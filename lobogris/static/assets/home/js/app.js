const app = [];
app.form = {
  inputs: function () {
    (function () {
      const modalForm = document.querySelector(".modal_form");
      const modalInput = modalForm.querySelectorAll("label");
      for (const input of modalInput) {
        input.classList.add("input__label", "input__label--haruki");
      }

      // trim polyfill : https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/Trim
      if (!String.prototype.trim) {
        (function () {
          // Make sure we trim BOM and NBSP
          const rtrim = /^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g;
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
    const buttonSend = document.querySelector(".js-sendForm");
    const valName = document.querySelector(".field__name");
    const valLastname = document.querySelector(".field__lastname");
    const valEmail = document.querySelector(".field__email");
    const error = document.querySelector(".error");

    const emailRegex =
      /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

    buttonSend.setAttribute("disabled", "");
    const emailRegexIsValid = emailRegex.test(valEmail.value);

    const nameIsEmpty = valName.value.length === 0;
    const lastnameIsEmpty = valLastname.value.length === 0;
    const emailIsEmpty = valEmail.value.length === 0;

    if (emailRegexIsValid) {
      valEmail.classList.remove("invalid");
      valEmail.classList.add("valid");
    } else {
      valEmail.classList.remove("valid");
      valEmail.classList.add("invalid");
    }

    if (nameIsEmpty && lastnameIsEmpty && emailIsEmpty) {
      buttonSend.setAttribute("disabled", "");
      console.log("ambos vacios");
    }

    valEmail.addEventListener("input", () => {
      if (emailRegex.test(valEmail.value)) {
        valEmail.classList.remove("invalid");
        valEmail.classList.add("valid");
        error.textContent = "";
        error.className = "error";
      } else {
        valEmail.classList.remove("valid");
        valEmail.classList.add("invalid");
        error.textContent = "Por favor, ingresar un correo electrónico válido.";
        error.className = "error active";
      }
      activateButton();
    });

    const activateButton = () => {
      if (valEmail.classList.contains("valid")) {
        buttonSend.removeAttribute("disabled");
      } else {
        buttonSend.setAttribute("disabled", "");
      }
    };
  },
  form: function () {
    const buttonForm = document.querySelector(".js-activeContactModal");
    const modal = document.querySelector(".modal");
    const buttonClose = document.querySelector(".material-symbols-sharp");
    buttonForm.addEventListener("click", function (e) {
      modal.classList.add("active");
      app.form.validate();
    });
    buttonClose.addEventListener("click", function (e) {
      modal.classList.remove("active");
    });
  },
  build: function () {
    app.form.inputs();
    app.form.form();
  },
};

window.addEventListener("load", (event) => {
  app.form.build();
});
