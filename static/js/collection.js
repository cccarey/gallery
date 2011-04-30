$(document).ready(function() {
	windowHeight = $(window).height() - 20;
	windowWidth = $(window).width() - 20;
	$('#images').galleria({
			height: windowHeight, 
			width: windowWidth, 
			autoplay: 3000, 
			transition: 'fade', 
			transitionSpeed: 1500
		});
	gallery = Galleria.get(0);
});
