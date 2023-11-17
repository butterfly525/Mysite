$(document).ready(function() {
    /*$('#toggle-symbol').click(function() {
        if(!$('#toggle').prop('checked')){

            $('aside').css({'left': '0px'});
            $('#toggle').prop('checked', false);
            $('#toggle-symbol').text("←");
        }
        else{
            $('aside').css({'left': '-225px'});
            $('#toggle').prop('checked', true);
            $('#toggle-symbol').text("→");
        }


    });*/

    /*  $('.nav-link').click(function(e) {
        e.preventDefault();
        $('aside').css({'left': '-225px'});
        var link = $(this).getAttribute('href');
        alert('#'+link);
        $('#'+link).scrollIntoView({
        block: 'nearest', behavior: 'smooth'
        });
        *//*$('#toggle').prop('checked', true);
        $('#toggle-symbol').text("→");*//*


    });*/
    $('a.nav-link[href^="#"]').on('click', function(event) {
        var target = $(this.getAttribute('href'));
        if(target.length) {
            event.preventDefault();
            $('html, body').stop().animate({
                scrollTop: target.offset().top
            }, 500);
        }
    });

    $('.btn-edit').click(function() {
        $(this).hide();
        var id = $(this).attr('id').replace('btn-edit-', '');
        $('#btn-save-' + id).show();
        $('#btn-cancel-' + id).show();
        $('.input-data-edit-' + id).show();
        $('[name="codeHTML-'+ id+'"]').css('height', $('[name="codeHTML-'+ id+'"]')[0].scrollHeight + 3 + 'px');
        $('[name="codeCSS-'+ id+'"]').css('height', $('[name="codeCSS-'+ id+'"]')[0].scrollHeight + 3 + 'px');
        $('[name="codeJS-'+ id+'"]').css('height', $('[name="codeJS-'+ id+'"]')[0].scrollHeight + 3 + 'px');
    });

    $('.btn-save').click(function(e) {
        e.preventDefault();
        var id = $(this).attr('id').replace('btn-save-', '');
        $(this).hide();
        $('.input-data-edit-' + id).hide();
        $('#btn-cancel-' + id).hide();
        $('#btn-edit-' + id).show();
        var codeHTML = $('textarea[name="codeHTML-'+id+'"]').val();
        var codeCSS = $('textarea[name="codeCSS-'+id+'"]').val();
        var codeJS = $('textarea[name="codeJS-'+id+'"]').val();
        var csrfToken = $('[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            url: '/save_data/' + id + '/',
            type: 'POST',
            data: {
            'codeHTML' : codeHTML,
            'codeCSS' : codeCSS,
            'codeJS' : codeJS,
            },
            headers: {
           'X-CSRFToken': csrfToken
            },
            success: function(response) {
                if (response.status === 'success') {
                    $.ajax({
                        url: window.location.pathname,
                        type: 'GET',
                        success: function(data) {
                            var newFeatures = $(data).find('#item-' + id);
                            if (newFeatures.length > 0) {
                                $('#item-' + id).html(newFeatures.html());
                            }
                        }
                    });
                } else {
                    console.log('Error saving data:', response.errors);
                }
            },
            error: function(response) {
                console.log('Error:', response.message);
            }
        });

    });

    $('.btn-cancel').click(function() {
        var id = $(this).attr('id').replace('btn-cancel-', '');
        $(this).hide();
        $('#btn-save-' + id).hide();
        $('#btn-edit-' + id).show();
        $('.input-data-edit-' + id).hide();
    });

    $('.btn-del').click(function() {
        var id = $(this).attr('id').replace('btn-cancel-', '');

    });
    $(window).on('scroll', function() {
        if ($(window).scrollTop() > 300) {
            $('#btn-up').css('opacity', '1');
            $('#btn-up').css('pointer-events', 'auto');
        } else {
            $('#btn-up').css('opacity', '0');
            $('#btn-up').css('pointer-events', 'none');
        }
    });
    $('#btn-up').on('click', function() {
        $('html, body').animate({scrollTop:0}, 50);
    });

  
});
