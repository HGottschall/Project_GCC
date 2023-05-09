$(document).ready(function() {
    $('#btn-home').addClass('btn-active');
});

// MUDAR PÁGINA
function ativarDiv(div, button) {
    $('.page').not(div).removeClass('active');
    $(div).addClass('active');

    $('.btn').not(button).removeClass('btn-active');
    $(button).addClass('btn-active')
};

// GIRAR CARDS
$(document).ready(function() {
    $('#teste').click(function() {
        if ($(this).closest('.card').hasClass('flip')) {
            $(this).closest('.card').removeClass('flip');
            $('.card-front').removeClass('disabled');
            $('.card-back').addClass('disabled');
        } else {
            $(this).closest('.card').addClass('flip');
            $('.card-front').addClass('disabled');
            $('.card-back').removeClass('disabled');
        }
    });
});


