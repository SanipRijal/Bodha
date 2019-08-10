$(window).scroll(function(){
	var top = $(window).scrollTop();
	if(top>=100){
		$("header").addClass('header-scroll')
	}

	else 
		if($("header").hasClass('header-scroll')){
			$("header").removeClass('header-scroll')		
		}
})


$('.banner-car').owlCarousel({
    loop: true,
    margin: 30,
    nav:false,
    dot:false,
    autoplay:true,
    animateOut: 'fadeOut',
    autoplayTimeout: 1000,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 1
        },
        1000: {
            items: 1
        }
    }
})

$('.events-car').owlCarousel({
    loop: true,
    margin: 0,
    nav:true,
    dot:false,
    autoplay:true,
    autoplayTimeout: 5000,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 2
        },
        1000: {
            items: 2
        }
    }
})



var btn = $('#top-button');

$(window).scroll(function() {
  if ($(window).scrollTop() > 300) {
    btn.addClass('show');
  } else {
    btn.removeClass('show');
  }
});

btn.on('click', function(e) {
  e.preventDefault();
  $('html, body').animate({scrollTop:0}, '300');
});

