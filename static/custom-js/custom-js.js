$(document).ready(function(){
        $("#header-index-id").hover(function(){
            $(this).removeClass('.header-index').addClass('.header-index2');
            $(this).removeClass('.header-index2').addClass('header-index');
        });
});