$(document).ready(function () {
    $("#run").on("input", function () {
        let value = this.value.replace(/[^0-9kK]/g, ""); 
        if (value.includes("-")) {
            let parts = value.split("-");
            value = parts[0]; 
        }
        if (value.length > 8) {
            value = value.slice(0, 8); 
        }
        if (value.length === 8) {
            const dv = calcularDV(value);
            this.value = value; 
        }
    });

    $("#run").on("blur", function () {
        let value = this.value.replace(/[^0-9kK]/g, ""); 

        if (value.length === 8) {
            const dv = calcularDV(value);
            this.value = `${value}-${dv}`; 
        }
    });

    const calcularDV = (rut) => {
        let suma = 0;
        let multiplicador = 2;
        for (let i = rut.length - 1; i >= 0; i--) {
            suma += parseInt(rut[i]) * multiplicador;
            multiplicador = multiplicador === 7 ? 2 : multiplicador + 1;
        }
        const resto = 11 - (suma % 11);
        if (resto === 11) {
            return '0';
        } else if (resto === 10) {
            return 'K';
        } else {
            return resto.toString();
        }
    };
});
