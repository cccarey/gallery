import web, config, os

from app.gallery import Gallery

render = config.render

class root:
    def GET(self, galleryName):
        gallerySplit = galleryName.split('/')
        if 'collection' in gallerySplit:
            if 'simple' in gallerySplit:
                collectionName = gallerySplit[3]
            else:
                collectionName = gallerySplit[2]
            galleryName = gallerySplit[0]
        
        gallery = Gallery(galleryName)
        
        if 'simple' in gallerySplit:
            if len(gallerySplit[4]) == 0:
                currentImage = gallery.getNextImage(collectionName)
            else:
                currentImage = gallerySplit[4]
            return render.simple(
                collectionName,
                gallery.getDiskPath(collectionName, currentImage, forDisk=False), 
                gallery.getPreviousImage(collectionName, currentImage), 
                gallery.getNextImage(collectionName, currentImage)
                )
        elif 'collection' in gallerySplit:
            return render.collection(gallery.getImages(collectionName))
        else:
            return render.gallery(gallery)
