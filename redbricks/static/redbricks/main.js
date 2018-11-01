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
    $('#my-pr').click(function(){
        $('.pr-card').toggle();
    });
});

//ajax-ratings
$(document).ready(function(){
//ratings
    $('.rat-btn').hover(function(e){

        if ($(this).attr('id') == '1st'){
            $('#1st').toggleClass('checked');
            $('#exampleModalLongTitle').html('Poor.. <i class="fa fa-thumbs-down" aria-hidden="true"></i>');
            $('#exampleModalLongTitle').css('color','red');
        }
        else if ($(this).attr('id') == '2nd'){
            $('#1st,#2nd').toggleClass('checked');
            $('#exampleModalLongTitle').html('Avarage...');
        }
        else if ($(this).attr('id') == '3rd'){
            $('#1st,#2nd,#3rd').toggleClass('checked');
            $('#exampleModalLongTitle').html('Good...');
        }
        else if ($(this).attr('id') == '4th'){
            $('#1st,#2nd,#3rd,#4th').toggleClass('checked');
            $('#exampleModalLongTitle').html('Very Good...');
        }
        else{
            $('#1st,#2nd,#3rd,#4th,#5th').toggleClass('checked');
            $('#exampleModalLongTitle').html('Excellent...');
        }
     });

    $('.rat-btn').click(function(e){
        e.preventDefault();
        rat_url = $('#rat-form').attr('rat_url');

        if ($(this).attr('id') == '1st'){
            var value = 1;
            $('#1st').toggleClass('checked');
        }
        else if ($(this).attr('id') == '2nd'){
            var value = 2;
            $('#1st,#2nd').toggleClass('checked');
        }
        else if ($(this).attr('id') == '3rd'){
            var value = 3;
            $('#1st,#2nd,#3rd').toggleClass('checked');
        }
        else if ($(this).attr('id') == '4th'){
            var value = 4;
            $('#1st,#2nd,#3rd,#4th').toggleClass('checked');
        }
        else{
            var value = 5;
            $('#1st,#2nd,#3rd,#4th,#5th').toggleClass('checked');
        }
        req=$.ajax({
            type:'POST',
            url:rat_url+'/post_review',
            data: {
                ratings: value,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                review: $('input[name=review]').val()
            }
        });
        req.done(function(){
            location.reload();
        })
     });
});

//profile-update

$(document).ready(function(){
    $('#email').click(function(e){
        e.preventDefault();
        $(this).fadeOut();
        $('#email-form').fadeIn();
    });
    $('#email-btn').click(function(){
        req = $.ajax({
            type:'POST',
            url: 'update/email',
            data:{
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                email: $('input[name=email]').val(),

            }

        });
    });

    $('.name').click(function(e){
        e.preventDefault();
        $(this).fadeOut();
        $('.name-form').fadeIn();
    });
    $('.name-btn').click(function(){
        req = $.ajax({
            type:'POST',
            url: 'update/full_name',
            data:{
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                full_name: $('input[name=full_name]').val(),
                 }

        });
    });
});