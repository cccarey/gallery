var Gallery = Backbone.Model.extend({
    baseUrl: gallery.config.serviceEndPoint + 'gallery',
    
    url: function() {
        return (this.id == null) ? this.baseUrl : this.baseUrl + "/" + this.id;
    },
    
    initialize: function() {
        _.bindAll(this, 
            'thumbExists'
        );
    },

    thumbExists: function() {
        return (this.get('thumb') == null);
    }
});

var Galleries = Backbone.Collection.extend({
    url: gallery.config.serviceEndPoint + 'gallery',
    
    model: Gallery,
    
    initialize: function() {
        _.bindAll(this);
    },

});

