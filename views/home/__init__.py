import web, config
import os

from app.gallery import Gallery

session = web.config._session
render = config.render

class root:
    def GET(self):
        gallery = Gallery('')
        return render.home(gallery.getGalleries())
    
