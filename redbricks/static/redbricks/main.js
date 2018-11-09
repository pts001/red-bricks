//map

// Initialize and add the map
function initMap() {
  // The location of Uluru
  var res_loc = {lat: -25.344, lng: 131.036};
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 4, center: res_loc});
  // The marker, positioned at Uluru
  var marker = new google.maps.Marker({position: res_loc, map: map});
}

//profile-card
$(document).ready(function(){
    $('#my-pr').click(function(e){
        e.preventDefault();
        $('.pr-card').toggle();
    });
});

//profile-update -- with ajax//

$(document).ready(function(){
    $(this).on('click','#pic',function(e){
        e.preventDefault();

    });
//update-email
    $(this).on('click','#username',function(e){
        e.preventDefault();
        $(this).fadeOut();
        $('#username-form').fadeIn();
    });
    $(this).on('click','#username-dismis',function(e){
        $('#username').fadeIn();
        $('#username-form').fadeOut();
        $('#username-alert').fadeOut();
    });
    $(this).on('click','#username-btn',function(){
        req = $.ajax({
            type:'POST',
            url: 'update/username',
            error: function (jqXHR, textStatus, errorThrown) {
                  $('#username-alert').fadeIn();
              },
            data:{
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                username: $('input[name=username]').val(),
                }
        });
        req.done(function(data){
            $('#item-0').fadeOut().fadeIn();
            $('#item-0').html(data);
        });
    });

//update-email
    $(this).on('click','#email',function(e){
        e.preventDefault();
        $(this).fadeOut();
        $('#email-form').fadeIn();
    });
    $(this).on('click','#email-dismis',function(e){
        $('#email').fadeIn();
        $('#email-form').fadeOut();
        $('email-alert').fadeOut();
    });
    $(this).on('click','#email-btn',function(){
        req = $.ajax({
            type:'POST',
            url: 'update/email',
            error: function (jqXHR, textStatus, errorThrown) {
                  $('#email-alert').fadeIn();
              },
            data:{
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                email: $('input[name=email]').val(),
                }
        });
        req.done(function(data){
            $('#item-1').fadeOut().fadeIn();
            $('#item-1').html(data);
        });
    });

//udate-name
    $(this).on('click','.name',function(e){
        e.preventDefault();
        $(this).fadeOut();
        $('.name-form').fadeIn();
    });
    $(this).on('click','.name-dismis',function(e){
        $('.name').fadeIn();
        $('.name-form').fadeOut();
    });
    $(this).on('click','.name-btn',function(){
        req = $.ajax({
            type:'POST',
            url: 'update/full_name',
            data:{
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                full_name: $('input[name=name]').val(),
                 }
        });
        req.done(function(data){
            $('#item-2').fadeOut().fadeIn();
            $('#item-2').html(data);
        });
    });

//update-city
    $(this).on('click','.city',function(e){
        e.preventDefault();
        $(this).fadeOut();
        $('.city-form').fadeIn();
    });
    $(this).on('click','.city-dismis',function(e){
        $('.city').fadeIn();
        $('.city-form').fadeOut();
    });
    $(this).on('click','.city-btn',function(){
        req = $.ajax({
            type:'POST',
            url: 'update/city',
            data:{
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                city: $('input[name=city]').val(),
                 }
        });
        req.done(function(data){
            $('#item-3').fadeOut().fadeIn();
            $('#item-3').html(data);
        });
    });
});