import os, mimetypes, datetime

class Gallery:
    def __init__(self, gallery):
        self.gallery = gallery
        self.rootHttpPath = ''
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

    def getGalleries(self):
        galleries = []
        for dir in self.dirs:
            if os.path.isdir(self.getDiskPath(dir)):
                gallery = Gallery(dir)
                counts = gallery.getCounts()
                galleries.append({
                    'name': dir,
                    'numCollections': counts[0],
                    'numImages': counts[1],
                    'coverThumb': gallery.getGalleryCoverThumbnail(),
                    'lastUpdate': counts[2]
                    })
        return galleries
    
    def getCounts(self, dir=None):
        collections = 0
        images = 0
        lastUpdate = None
        if dir is None:
            dirs = self.dirs
        else:
            dirs = os.listDir(self.getDiskPath(dir))
        for item in dirs:
            if os.path.isdir(self.getDiskPath(item)):
                collections = collections + 1
                images = images + self.getImageCount(item)
                updated = datetime.datetime.fromtimestamp(os.path.getmtime(self.getDiskPath(item)))
                if lastUpdate is None or lastUpdate < updated:
                    lastUpdate = updated
            else:
                mimetype = mimetypes.guess_type(self.getDiskPath(item))[0]
                if mimetype is not None and "image" in mimetype:
                    images = images + 1
        lastUpdateFmt = lastUpdate.strftime("%x %X")
        return (collections, images, lastUpdateFmt)
        
    def getCollectionCount(self):
        collections = 0
        for dir in self.dirs:
            if os.path.isdir(self.getDiskPath(dir)):
                collections = collections + 1
        return collections
        
    def getCollections(self):
        collections = []
        for dir in self.dirs:
            if os.path.isdir(self.getDiskPath(dir)):
                collections.append({
                    'name': dir,
                    'numImages': self.getImageCount(dir),
                    'coverThumb': self.getCoverThumbnail(dir),
                    'lastUpdateFmt': datetime.datetime.fromtimestamp(os.path.getmtime(self.getDiskPath(dir))).strftime("%x %X")
                    })
        return collections
    
    def getGalleryCoverThumbnail(self):
        coverThumb = ""
        for dir in self.dirs:
            if os.path.isdir(self.getDiskPath(dir)):
                coverThumb = self.getCoverThumbnail(dir)
            if len(coverThumb) > 0:
                return coverThumb
        return coverThumb
        
    def getCoverThumbnail(self, dir):
        files = os.listdir(self.getDiskPath(dir))
        coverThumb = ""
        for file in files:
            if not os.path.isdir(self.getDiskPath(dir, file)):
                if "cover" in file and os.path.exists(self.getDiskPath(dir, file, forThumbs=True)):
                    if "image" in mimetypes.guess_type(self.getDiskPath(dir, file, forThumbs=True))[0]:
                        coverThumb = self.getDiskPath(dir, file, forDisk=False, forThumbs=True)
                elif len(coverThumb) == 0 and os.path.exists(self.getDiskPath(dir, file, forThumbs=True)):
                    if "image" in mimetypes.guess_type(self.getDiskPath(dir, file, forThumbs=True))[0]:
                        coverThumb = self.getDiskPath(dir, file, forDisk=False, forThumbs=True)
        return coverThumb
        
    def getImageCount(self, dir):
        # getImages is pretty involved... do it simpler (though this is more difficult to maintain)
        images = 0
        files = os.listdir(self.getDiskPath(dir))
        for file in files:
            if not os.path.isdir(self.getDiskPath(dir, file)):
                images = images + 1
            else:
                images = images + self.getImageCount("%s/%s" % (dir, file))
        return images

    def getImages(self, dir):
        images = []
        try:
            files = os.listdir(self.getDiskPath(dir))
            files.sort()
            for file in files:
                if not os.path.isdir(self.getDiskPath(dir, file)):
                    if "image" in mimetypes.guess_type(self.getDiskPath(dir, file))[0]:
                        if not os.path.exists(self.getDiskPath(dir, forThumbs=True)):
                            os.makedirs(self.getDiskPath(dir, forThumbs=True))
                        if not os.path.exists(self.getDiskPath(dir, file, forThumbs=True)):
                            ret = os.system(
                                "convert -resize 5%% '%s' '%s'" % 
                                    (
                                        self.getDiskPath(dir, file), 
                                        self.getDiskPath(dir, file, forThumbs=True)
                                    )
                                )
                        images.append({
                            'name': file, 
                            'image': self.getDiskPath(dir, file, forDisk=False),
                            'thumb': self.getDiskPath(dir, file, forDisk=False, forThumbs=True),
                            'type': mimetypes.guess_type(self.getDiskPath(dir, file))[0]
                            })
        except:
            pass
        return images

