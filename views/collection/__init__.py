import web, config
import os

from app.gallery import Gallery

render = config.render

class root:
    def GET(self, galleryName, collection):
        gallery = Gallery(galleryName)
        return render.collection(gallery.getImages(collection))
    
