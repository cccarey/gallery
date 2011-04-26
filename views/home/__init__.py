import web, config
import os

from app.gallery import Galleries

session = web.config._session
render = config.render

class root:
    def GET(self):
        galleries = Galleries()
        return render.home(galleries.getGalleries())
    