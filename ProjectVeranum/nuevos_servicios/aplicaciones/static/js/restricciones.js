$(document).ready(function () {

    $("#nombre").on("input" , function(){
        this.value = this.value.replace(/[^A-Za-z]/g, "");
    });

    $("#run").on("input" , function(){
        this.value = this.value.replace(/\D/g, "");
    });

    $("#email").on("input", function () {
        const emailPattern = /^[a-zA-Z0-9._%+-]+@gmail\.(com|cl)$/;
        const emailValue = $(this).val();
        if (!emailPattern.test(emailValue)) {
            $("#emailError").text("Debe ser un correo @gmail.com o @gmail.cl");
        } else {
            $("#emailError").text("");
        }
    });

    // Manejo de contraseña: Mostrar y Ocultar
    $("#togglePassword").on("click", function () {
        const passwordField = $("#pass");
        const fieldType = passwordField.attr("type") === "password" ? "text" : "password";
        passwordField.attr("type", fieldType);
        $(this).text(fieldType === "password" ? "Mostrar" : "Ocultar");
    });

});