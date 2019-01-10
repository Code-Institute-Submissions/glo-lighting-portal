			$(document).ready(function(){
				$('.gallery').featherlightGallery({
					gallery: {
						fadeIn: 300,
						fadeOut: 300
					},
					openSpeed:    300,
					closeSpeed:   300
				});
				$('.gallery2').featherlightGallery({
					gallery: {
						next: 'next »',
						previous: '« previous'
					},
					variant: 'featherlight-gallery2'
				});
			});

		
