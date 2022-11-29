const gulp = require("gulp");
const sass = require("gulp-sass")(require("sass"));
const uglify = require("gulp-uglify-es").default;
const concat = require("gulp-concat");
var version = require("gulp-version-number");
const browser = require("browser-sync").create();

const vconfig = {
  value: "%MDS%",
  append: {
    key: "v",
    to: ["css", "js"],
  },
  output: {
    file: "version.json",
  },
};

sass.compiler = require("node-sass");

let paths = {
  scripts: {
    src: "./assets/js/modules/**/*.js",
    dest: "./js",
  },
  vendor: {
    src: "./assets/js/plugins/**/*.js",
    dest: "./js",
  },
};

gulp.task("styles", () => {
  return gulp
    .src("./assets/sass/*.scss")
    .pipe(
      sass({
        outputStyle: "expanded",
      })
    )
    .pipe(gulp.dest("./css/"))
    .pipe(browser.stream());
});

gulp.task("javascript", () => {
  return gulp
    .src(paths.scripts.src, {
      sourcemaps: true,
    })
    .pipe(concat("app.js"))
    .pipe(uglify())
    .pipe(gulp.dest(paths.scripts.dest))
    .pipe(browser.stream());
});

gulp.task("vendor", () => {
  return gulp
    .src(paths.vendor.src, {
      sourcemaps: true,
    })
    .pipe(concat("vendor.js"))
    .pipe(gulp.dest(paths.vendor.dest))
    .pipe(browser.stream());
});

gulp.task("versions", () => {
  return gulp
    .src("./dist/**/*.html")
    .pipe(version(vconfig))
    .pipe(gulp.dest("./dist/"))
    .pipe(browser.stream());
});

gulp.task("watch", () => {
  gulp.watch("./assets/sass/*.scss", gulp.series("styles"));
  gulp.watch("./assets/js/**/*.js", gulp.series("javascript"));
});

gulp.task("default", gulp.parallel("styles", "watch", "versions"));

/*
gulp.task(
  "default",
  gulp.parallel("styles", "watch", "javascript", "vendor", "versions")
);
*/
