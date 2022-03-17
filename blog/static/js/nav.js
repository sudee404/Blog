$(document).ready(function () {
    var navbtn = $(".nav-link");
    var headline = $("#headline");
    navbtn.mouseenter(function () {
        $(this).addClass("text-warning");
        $(this).mouseleave(function () {
            $(this).removeClass("text-warning");
        });
    });
    headline.mouseenter(function () {
        $(this).addClass("text-success");
        $(this).mouseleave(function () {
            $(this).removeClass("text-success");
        });
    });
});
