$(document).ready(function() {
    $(document).bind('keypress', function(e) {
        if (e.keyCode == 44) { document.location = $("a#previous").attr('href'); }
        if (e.keyCode == 46) { document.location = $("a#next").attr('href'); }
    });
});
