function sideNav() {
  if ($(window).width() < 769) {
    $('.off-canvas-wrap').removeClass('move-right');
    $('.left-off-canvas-toggle').show();
  } else {
    $('.off-canvas-wrap').addClass('move-right');
    $('.left-off-canvas-toggle').hide();
  }
}

$(window).resize(function() {
  sideNav();
});

$(document).ready(function() {
  $('.item').on('click', function() {
    elementId = this.getAttribute('href');
    $('.item').removeClass('active');
    $(this).addClass('active');
    $('#dashboard').addClass('hide');
    $('#new-event').addClass('hide');
    $('#recent-activity').addClass('hide');
    $(elementId).removeClass('hide');
  });
});
