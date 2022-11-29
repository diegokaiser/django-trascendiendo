var app = [];
app.form = {
  inputs: function () {
    (function () {
      var modalForm = document.querySelector(".modal_form");
      var modalInput = modalForm.querySelectorAll("label");
      for (const input of modalInput) {
        input.classList.add("input__label", "input__label--haruki");
      }

      // trim polyfill : https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/Trim
      if (!String.prototype.trim) {
        (function () {
          // Make sure we trim BOM and NBSP
          var rtrim = /^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g;
          String.prototype.trim = function () {
            return this.replace(rtrim, "");
          };
        })();
      }

      [].slice
        .call(document.querySelectorAll("input.input__field"))
        .forEach(function (inputEl) {
          // in case the input is already filled..
          if (inputEl.value.trim() !== "") {
            classie.add(inputEl.parentNode, "input--filled");
          }

          // events:
          inputEl.addEventListener("focus", onInputFocus);
          inputEl.addEventListener("blur", onInputBlur);
        });

      function onInputFocus(ev) {
        classie.add(ev.target.parentNode, "input--filled");
      }

      function onInputBlur(ev) {
        if (ev.target.value.trim() === "") {
          classie.remove(ev.target.parentNode, "input--filled");
        }
      }
    })();
  },
  validate: function () {
    var buttonSend = document.querySelector(".js-sendForm");
    buttonSend.setAttribute("disabled", "");
  },
  form: function () {
    var buttonForm = document.querySelector(".js-activeContactModal");
    var modal = document.querySelector(".modal");
    var buttonClose = document.querySelector(".material-symbols-sharp");
    buttonForm.addEventListener("click", function (e) {
      modal.classList.add("active");
    });
    buttonClose.addEventListener("click", function (e) {
      modal.classList.remove("active");
    });
  },
  build: function () {
    app.form.inputs();
    app.form.validate();
    app.form.form();
  },
};

window.addEventListener("load", (event) => {
  app.form.build();
});
