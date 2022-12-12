const app = [];
app.forms = {
  styles: function () {
    const form = document.querySelector("form");
    const divsForm = form.querySelectorAll(":scope > div");
    const labelsForm = form.querySelectorAll(":scope > div > label");
    for (const div of divsForm) {
      div.classList.add("mb-3");
    }
    for (const label of labelsForm) {
      label.classList.add("form-label");
    }
  },
  build: function () {
    app.forms.styles();
  },
};

window.addEventListener("load", (event) => {
  app.forms.build();
});
