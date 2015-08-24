//make column full height of page
$(document).ready(function(){
	$("#left").height( $(".container-fluid").height() );

});


//make td into a link
$(document).ready(function() {
    $('td[data-href]').on("click", function() {
      document.location = $(this).data('href');
 
    });
});

//keep one element in closed accordion
$('.panel-heading a').on('click',function(e){
    if($(this).parents('.panel').children('.panel-collapse').hasClass('in')){
        e.preventDefault();
        e.stopPropagation();
    }
});

/*//Add Hover effect to menus
jQuery('ul.nav li.dropdown').hover(function() {
  jQuery(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn();
}, function() {
  jQuery(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut();
})*/;