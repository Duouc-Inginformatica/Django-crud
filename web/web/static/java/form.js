$(document).ready(function(){
    
    $("input").blur(function(){
        if ($(this).val() != ""){
            $(this).parent().css({"color":"black"});
            $(this).css({"border-bottom":"1px solid silver","color":"gray"});                 
        }
    })
    
    //--- CONTINUE ---
    $("form > p > a").click(function(){
        //-- only example
        var Datos = {};
        Datos.rut = $("input[name='rut']").val();
        Datos.nombre = $("input[name='nombre']").val();
        Datos.apellido_pat = $("input[name='apellido_pat']").val();
        Datos.apellido_mat = $("input[name='apellido_mat']").val();
        Datos.edad = $("input[name='edad']").val();
        Datos.vacuna = $("input[name='vacuna']").val();
        Datos.fecha = $("input[name='fecha']").val();

        //-- Validator            
        $("input").each(function(e, valor){
            var error = false;
            if ($(this).val() == ""){
                error = true;
            }
            if (error === true){
                //-- with errors
                $(this).parent().css({"color":"red"});
                $(this).css({"border-bottom":"1px solid red"});
            }else{
                //-- without errors
                $(this).parent().css({"color":"black"});
                $(this).css({"border-bottom":"1px solid silver","color":"gray"}); 
            }
        })

        //-- msg example
        $("body").append(JSON.stringify(Datos) + "<br>");
    })
})