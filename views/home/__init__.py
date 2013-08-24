import web, config
import os

from app.gallery import Gallery

render = config.render

class scan:
    def GET(self):
        Gallery('').scan()
        raise web.seeother('.')
        
class root:
    def GET(self):
        gallery = Gallery('')
        return render.home(gallery.get_galleries())
    
