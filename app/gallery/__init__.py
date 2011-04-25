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
        files = os.listdir('%s/%s' % (self.diskPath, dir))
        files.sort()
        for file in files:
            if not os.path.isdir('%s/%s/%s' % (self.diskPath, dir, file)):
                images.append({'name': file, 'url': '%s/%s/%s' % (self.httpPath, dir, file)})
        return images