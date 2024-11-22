$(document).ready(function () {

    $("#run").on("input" , function(){
        this.value = this.value.replace(/\D/g, "");
    });

    $("#nombre").on("input" , function(){
        this.value = this.value.replace(/[^A-Za-z]/g, "");
    });

    $("#fono").on("input", function (){
        this.value = this.value.replace(/\D/g,"")
    })

    $("#direccion").on("input", function(){
        this.value = this.value.replace(/[^A-Za-z]/g, "")
    })

    $("#profesion").on("input" , function(){
        this.value = this.value.replace(/[^A-Za-z]/g, "")
    })
    $("ocupacion").on("input", function(){
        this.value = this.value.replace(/[^A-Za-z]/g, "")
    })

    $("puesto").on("input", function(){
        this.value = this.value.replace(/[^A-Za-z]/g, "")
    })

});