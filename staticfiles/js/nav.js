$(document).ready(function () {
    var navbtn = $(".nav-link");
    var headline = $("#headline");
    navbtn.mouseenter(function () {
        $(this).addClass("text-warning");
        $(this).mouseleave(function () {
            $(this).removeClass("text-warning");
        });
    });
    
});
