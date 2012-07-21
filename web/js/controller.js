var controller = {
    baseUrl: '/api/xml/',
	
	init: function() {
	    _.bindAll(
	        this, 
	        "getRawEndpoint",
            "makeCall"
	    );
    	this.view = new ArchitectureView({el:$("body")});
	    this.view.render();
	    return this;
	},
    
	getRawEndpoint: function() {
	    this.makeCall($("#api-endpoint").val(), this.view.populateRawResult, null);
	    return false;
	},
	
	makeCall: function(uri, successFunc, params) {
	    var errorFunc = this.view.alertScopeError;
        var url = this.baseUrl + uri;
        if (params != null) {
            $.each(params, function(key,val) {
                url = url + "&" + key + "=" + val;
            });
        }
        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'xml',
            success: successFunc,
            error: errorFunc
        });
	}
}

$(function() {
    window.app = controller.init();
});
