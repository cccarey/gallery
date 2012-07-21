var GalleriesView = Backbone.View.extend({
    events: {
        "click #getRawEndpoint"     : "handleGetRawEndpointClick"
    },
    
    initialize: function() {
        _.bindAll(this, 
            "populateResult",
            "alertError"
        );
    },
    
    render: function() {
        this.el.html(ich.template({}));
        this.resultEl = $("#result");
    },
    
    handleGetRawEndpointClick: function() { 
        this.resultEl.hide('slow', function() { app.getRawEndpoint(); });
        return false;
    },    
    
    populateResult: function(data) {
        var jsonData = $.xml2json(data);
        new RawJsonObjectView({model: jsonData, el:this.resultEl}).render();
        this.resultEl.show('slow');
    },
    
	alertError: function(req, status, error) {
		this.resultEl.html('<p>Issue loading Projects')
			.append('<p>Status: ' + status)
			.append('<p>Error: ' + error);
        this.resultEl.show('slow');
	}
});

