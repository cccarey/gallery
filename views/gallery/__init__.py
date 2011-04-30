import web, config, os

from app.gallery import Gallery

session = web.config._session
render = config.render

class root:
    def GET(self, galleryName):
        if '/' in galleryName:
            collectionName = galleryName.rpartition('/')[2]
            galleryName = galleryName.partition('/')[0]
            gallery = Gallery(galleryName)
            return render.collection(gallery.getImages(collectionName))
        else:
            return render.gallery(Gallery(galleryName))
