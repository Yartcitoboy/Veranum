$(document).ready(function () {
  $("#contact_form")
    .bootstrapValidator({
      // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
      feedbackIcons: {
        valid: "glyphicon glyphicon-ok",
        invalid: "glyphicon glyphicon-remove",
        validating: "glyphicon glyphicon-refresh",
      },
      fields: {
        nombre: {
          validators: {
            stringLength: {
              Request: true,
              min: 2,
            },
            notEmpty: {
              message: "Por favor proporcione su nombre",
            },
          },
        },
        run: {
          validators: {
            stringLength: {
              Request: true,
              min: 8,
            },
            notEmpty: {
              message: "Por favor proporcione su run",
            },
          },
        },
        email: {
          validators: {
            stringLength: {
              Request: true,
            },
            notEmpty: {
              message: "Por favor proporcione su correo electronico",
            },
          },
        },
        password: {
          validators: {
            stringLength: {
              Request: true,
              min: 6,
            },
            notEmpty: {
              message: "Por favor proporcione una contraseña",
            },
          },
        },
        sexo: {
          validators: {
            Request: true,
            notEmpty: {
              message: "Por favor seleccione su sexo",
            },
          },
        },
      },
    })
    .on("success.form.bv", function (e) {
      $("#success_message").slideDown({ opacity: "show" }, "slow"); // Do something ...
      $("#contact_form").data("bootstrapValidator").resetForm();

      // Prevent form submission
      e.preventDefault();

      // Get the form instance
      var $form = $(e.target);

      // Get the BootstrapValidator instance
      var bv = $form.data("bootstrapValidator");

      // Use Ajax to submit form data
      $.post(
        $form.attr("action"),
        $form.serialize(),
        function (result) {
          console.log(result);
        },
        "json"
      );
    });
});
