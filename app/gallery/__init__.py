import os, mimetypes

class Gallery:
    def __init__(self, gallery):
        self.gallery = gallery
        self.rootHttpPath = 'http://localhost:8080'
        self.rootPath = os.getcwd()
        self.gallerySubPath = 'static/galleries'
        self.thumbSubPath = 'static/thumbs'
        self.dirs = os.listdir(self.getDiskPath())
        self.dirs.sort()

    def getDiskPath(self, dir=None, file=None, forDisk=True, forThumbs=False):
        root = self.rootPath if forDisk else self.rootHttpPath
        path = self.thumbSubPath if forThumbs else self.gallerySubPath
        pathEle = [root, path, self.gallery]
        if dir:
            pathEle.append(dir)
        if file:
            pathEle.append(file)
        
        return '/'.join(pathEle)
        
    def getCollections(self):
        collections = []
        for dir in self.dirs:
            if os.path.isdir(self.getDiskPath(dir)):
                collections.append({'name': dir})
        return collections
    
    def getImages(self, dir):
        images = []
        try:
            files = os.listdir(self.getDiskPath(dir))
            files.sort()
            for file in files:
                if not os.path.isdir(self.getDiskPath(dir, file)):
                    if "image" in mimetypes.guess_type(self.getDiskPath(dir, file))[0]:
                        images.append({
                            'name': file, 
                            'image': self.getDiskPath(dir, file, forDisk=False),
                            'type': mimetypes.guess_type(self.getDiskPath(dir, file))[0]
                            })
        except:
            pass
        return images
    
class Galleries:
    def __init__(self):
        self.subPath = 'static/galleries'
        self.diskPath = '%s/%s' % (os.getcwd(), self.subPath)
        
    def getGalleries(self):
        galleries = []
        dirs = os.listdir(self.diskPath)
        dirs.sort()
        for dir in dirs:
            if os.path.isdir('%s/%s' % (self.diskPath, dir)):
                galleries.append({'name': dir})
        return galleries
