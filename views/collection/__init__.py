import web, config
import os

from app.gallery import Gallery

render = config.render

class root:
    def GET(self, gallery_name, collection):
        gallery = Gallery(gallery_name)
        return render.collection(gallery.get_images(collection))
    
