import os

class Gallery:
    def __init__(self, gallery):
        self.gallery = gallery
        self.subPath = 'static/galleries'
        self.diskPath = '%s/%s/%s' % (os.getcwd(), self.subPath, self.gallery)
        self.httpPath = 'http://localhost:8080/%s/%s' % (self.subPath, self.gallery)
        self.dirs = os.listdir(self.diskPath)
        
    def getCollections(self):
        collections = []
        for dir in self.dirs:
            if os.path.isdir('%s/%s' % (self.diskPath, dir)):
                collections.append({'name': dir})
        return collections
    
    def getImages(self, dir):
        images = []
        try:
            files = os.listdir('%s/%s' % (self.diskPath, dir))
            files.sort()
            for file in files:
                if not os.path.isdir('%s/%s/%s' % (self.diskPath, dir, file)):
                    images.append({'name': file, 'url': '%s/%s/%s' % (self.httpPath, dir, file)})
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
        for dir in dirs:
            if os.path.isdir('%s/%s' % (self.diskPath, dir)):
                galleries.append({'name': dir})
        return galleries
