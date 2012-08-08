$(document).ready(function() {
    getDetails = function(data) {
        var title = (data.xmp["Xmp.dc.title"]) ? 
                data.xmp["Xmp.dc.title"].raw_value["x-default"] : 
                null;
        var desc = (data.xmp["Xmp.dc.description"]) ? 
                data.xmp["Xmp.dc.description"].raw_value["x-default"] : 
                null;
        var comment = (data.comment.length > 0) ? data.comment : null;
        var rating = (data.xmp["Xmp.xmp.Rating"]) ? data.xmp["Xmp.xmp.Rating"].raw_value : null;
        var editMsg = null;
        $('#title').html((title) ? title : editMsg);
        $('#title-edit').val($('#title').html());
        $('#description').html((desc) ? desc : editMsg);
        $('#description-edit').val($('#description').html());
        $('#comment').html((comment) ? comment : editMsg);
        $('#comment-edit').val($('#comment').html());
        $('#rating').html((rating) ? rating : editMsg);
        $('#dimensions-x').html(data.dimensions[0]);
        $('#dimensions-y').html(data.dimensions[1]);
    };
    
    showDetails = function() {
        $(this).addClass("highlight");
        srcSplit = $(this).attr('src').split("/")
        $("#gallery-id").val(srcSplit[srcSplit.length - 3]);
        $("#collection-id").val(srcSplit[srcSplit.length - 2]);
        $("#image-id").val(srcSplit[srcSplit.length - 1]);
        $.ajax({
            type: 'GET',
            url: api.basedir + '/api/image/metadata/' + 
                $("#gallery-id").val() + '/' + 
                $("#collection-id").val() + '/' + 
                $("#image-id").val(),
            success: getDetails
        });
        $('#image-details').show();
    };
    
    hideDetails = function() {
        $(this).removeClass("highlight");
        return;
        $('#image-details').hide();
    };
    
    $('.thumb').hoverIntent({
        sensitivity: 3,
        interval: 200,
        timeout: 200,
        over: showDetails,
        out: hideDetails
    });

    $('#title-label, #title, #description-label, #description, #comment-label, #comment').click(function(event) {
        var eleBaseName = event.currentTarget.id;
        if (eleBaseName.indexOf("label") != -1) {
            eleBaseName = eleBaseName.split('-')[0];
        }
        $('#' + eleBaseName).hide(200, function() {
            $('#' + eleBaseName + '-edit').show(200, function() { 
                $('#' + eleBaseName + '-edit').focus();
                if ($('#' + eleBaseName + '-edit').is('textarea')) {
                    $('#' + eleBaseName + '-edit').height(
                        ($('#' + eleBaseName).height() > 120) ?
                            $('#' + eleBaseName).height() :
                            120
                    );
                }
            }); 
        });
    });

    $('#title-label, #title').dblclick(function() {
        $('#title-edit').val($("#image-id").val());
        $(this).click();
    });
    
    $('#title-edit, #description-edit, #comment-edit').keyup(function(event) {
        if (event.keyCode != 13 && event.keyCode != 27) return;
        
        var eleBaseName = event.currentTarget.id.split('-')[0];

        if (event.keyCode == 13) {
            var tag_key;
            if (eleBaseName == "title") {
                tag_key = "Xmp.dc.title";
            } else if (eleBaseName == "description") {
                tag_key = "Xmp.dc.description";
            } else {
                tag_key = "comment"
            }
            $.ajax({
                type: 'POST',
                url: api.basedir + '/api/image/metadata/' + 
                    $("#gallery-id").val() + '/' +
                    $("#collection-id").val() + '/' +
                    $("#image-id").val() + '/' +
                    tag_key,
                data: { "value": $("#" + eleBaseName  + "-edit").val() },
                success: function() {
                    $("#" + eleBaseName).html($("#" + eleBaseName  + "-edit").val());
                },
                error: function() {
                    $("#" + eleBaseName + "-edit").val($("#" + eleBaseName + "-edit").html());
                }
            });
        }
        
        $('#' + eleBaseName + '-edit').hide(200, function() { $('#' + eleBaseName).show(200); });
    });
});

