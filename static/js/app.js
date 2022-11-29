console.log("script");

var app = [];
app.form = {
  inputs: function () {},
  validate: function () {},
  form: function () {},
  build: function () {
    console.log("app.form.build running");
    app.form.inputs();
    app.form.validate();
    app.form.form();
  },
};

window.addEventListener("load", (event) => {
  console.log("pagina cargada completamente");
  app.form.build();
});
