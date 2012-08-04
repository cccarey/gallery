$(document).ready(function() {
    var totalImages = $('img').length;
    var currImages = 0;
    
    $('img').load(function() {
        currImages = currImages + 1;
        if (currImages == totalImages) {
            var max_height = 0;
            $(".item").each(function() {
                if ($(this).height() > max_height) max_height = $(this).height();
            });
            
            $(".item").each(function() { $(this).height(max_height); });
        }
    });
});
