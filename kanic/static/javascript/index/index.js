$(document).ready(function() {

    // Scroll to bottom if newsletter email is invalid
    if($('#newsletterform > ul').length > 0) {
        window.scrollTo(0, document.body.scrollHeight);
    }

    // Disable career page's title input
    $('#id_title').prop('disabled', true);
    
    // change navigation bar when page is loaded
    var top = $(document).scrollTop();
    if(top > 200) {
        $('.navbar').removeClass('navbar-transparent');
        $('.navbar-default .navbar-nav > li > a').css('color', 'black');
        $('.navbar-default .navbar-brand').css('color', 'black');
    } else {
        $('.navbar').addClass('navbar-transparent');
        $('.navbar-default .navbar-nav > li > a').css('color', 'white');
        $('.navbar-default .navbar-brand').css('color', 'white');
    }
    // listening to scrolling action
    $(window).scroll(function () {
        var top = $(document).scrollTop();

        if(top > 200) {
            $('.navbar').removeClass('navbar-transparent');
            $('.navbar-default .navbar-nav > li > a').css('color', 'black');
            $('.navbar-default .navbar-brand').css('color', 'black');
        } else {
            $('.navbar').addClass('navbar-transparent');
            $('.navbar-default .navbar-nav > li > a').css('color', 'white');
            $('.navbar-default .navbar-brand').css('color', 'white');
        }

        if(top > 395) {
            $('div.left').css('-webkit-transform', 'translateX(0px)');
            $('div.middle').css('-webkit-transform', 'translateY(0px)');
            $('div.right').css('-webkit-transform', 'translateX(0px)');
        }

        if(top > 740) {
            $('div.left-upper, div.left-lower, div.right-upper, div.right-lower')
            .css('-webkit-transform', 'translate(0px, 0px)');
        }
    });

    // trigger css in main section to animate(eg. transition)
    $('.landing-section').css('top', '40%');
    $('.main-line, .main-title').css('color', 'rgba(255, 255, 255, 1)');
    $('button.signup').css('color', 'rgba(255, 255, 255, 1)');
    $('button.signup').css('background-color', 'rgba(255, 255, 255, 0)');

    // Focus on modol's field
    $('#myModal').on('shown.bs.modal', function () {
        $('#id_name').focus()
    });

    // If form submmited is not valid, form will appear again with errors
    if($('#carOwner_invalid').length) {
        $('#CarOwnerModal').modal('toggle');
    }

    // If form submmited is not valid, form will appear again with errors
    if($('#mechanic_invalid').length) {
        $('#MechanicModal').modal('toggle');
    }

    // Disable submit button after clicked
    $('#mechanic_submit').on('submit', function() {
        $('#mechanic_submit').prop('disabled', true);
    });

    // Disable submit button after clicked
    $('#submit').on('submit', function() {
        $('#submit').prop('disabled', true);
    });


});
