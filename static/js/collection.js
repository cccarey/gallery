$(document).ready(function() {
	windowHeight = $(window).height() - 20;
	windowWidth = $(window).width() - 20;
	$('#images').galleria({
			height: windowHeight, 
			width: windowWidth, 
			transition: 'fade', 
			autoplay: 3000,
			transitionSpeed: 1500,
			extend: function() {
			    this.attachKeyboard({
			        left: this.prev,
			        right: this.next,
			        up: function() {
			            this.play(3000);
		            },
			        down: this.pause
			    });
			}
		});
	gallery = Galleria.get(0);
});
