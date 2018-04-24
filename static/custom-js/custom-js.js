$(document).ready(function(){
  $("#more-info-section p").hide();
  $("#intro-section p").hide();
  $('#more-info-section h2').on('click', function() {
    $('#more-info-section p').animate({
        'height': 'toggle'
    }, 1000);
});
  $('#intro-section h2').on('click', function() {
    $('#intro-section p').animate({
        'height': 'toggle'
    }, 1000);
});
});