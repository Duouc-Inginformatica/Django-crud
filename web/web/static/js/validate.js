// usando jquery para validar el formulario
$("#form_ins").validate({
    rules: {
        rut : {
            required: true,
            rut: true
        },
        nombres : {  
            required: true,
            minlength: 3
        },
        apellidos : {
            required: true,
            minlength: 3
        },
        correos : {
            required: true,
            email: true
        },
        ticket : {
            required: true,
            minlength: 3
        },
        edad : {
            required: true,
            minlength: 1,
            number: true,
            min: 1,
            max: 100

        },
        fecha : {
            required: true,
            minlength: 1
        },
        submitHandler: function(){
            // when no errors
        }
    }    
 })