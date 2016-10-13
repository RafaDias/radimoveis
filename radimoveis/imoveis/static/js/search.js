$("#learn-more").on('click', function (event) {
    if (this.hash !== "") {
        event.preventDefault();
        var hash = this.hash;
        $('html, body').animate({
            scrollTop: $(hash).offset().top
        }, 800, function () {
            $("#search").select();
        });
    }
});

$("#submitSearch").on('click', function (event) {
    event.preventDefault();
    $("form").submit();
});

$('form').submit(function () {
    if ($('input').val() === "") {
        $("#search")
            .select()
            .css({"border": '#FF0000 1px solid'})
            .prop("placeholder", "Por favor, digite o local desejado.");
        return false;
    }
});