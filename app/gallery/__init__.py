import os, mimetypes, datetime, PythonMagick, json, time

from config import THUMB_WIDTH, BASEDIR, IMAGE_PATHS, GALLERIES_CACHE_LIFE

class Gallery:
    def __init__(self, gallery):
        self.gallery = gallery
        self.dirs = os.listdir(self.get_disk_path())
        self.dirs.sort()

    def get_disk_path(self, dir=None, file=None, for_disk=True, for_thumbs=False):
        root = IMAGE_PATHS['disk_root'] if for_disk else IMAGE_PATHS['http_root']
        path = IMAGE_PATHS['thumbs'] if for_thumbs else IMAGE_PATHS['galleries']
        pathEle = [root, path, self.gallery]
        if dir:
            pathEle.append(dir)
        if file:
            pathEle.append(file)
        
        return '/'.join(pathEle)

    def get_galleries(self):
        galleries = None
        if os.path.exists('galleries.json') and (time.time() - os.path.getmtime('galleries.json') < GALLERIES_CACHE_LIFE):
            galleries_store = open('galleries.json', 'r')
            try:
                galleries = json.load(galleries_store)
            except:
                pass
            finally:
                galleries_store.close()
            
        if galleries is not None: return galleries
            
        galleries = []
        for dir in self.dirs:
            if os.path.isdir(self.get_disk_path(dir)):
                gallery = Gallery(dir)
                counts = gallery.get_counts()
                galleries.append({
                    'name': dir,
                    'num_collections': counts[0],
                    'num_images': counts[1],
                    'cover_thumb': gallery.get_gallery_cover_thumbnail(),
                    'last_update': counts[2]
                    })
        galleries_store = open('galleries.json', 'w')
        json.dump(galleries, galleries_store, indent=2)
        galleries_store.close()
        return galleries
    
    def get_counts(self, dir=None):
        collections = 0
        images = 0
        last_update = None
        if dir is None:
            dirs = self.dirs
        else:
            dirs = os.listDir(self.get_disk_path(dir))
        for item in dirs:
            if os.path.isdir(self.get_disk_path(item)):
                collections = collections + 1
                images = images + self.get_image_count(item)
                updated = datetime.datetime.fromtimestamp(os.path.getmtime(self.get_disk_path(item)))
                if last_update is None or last_update < updated:
                    last_update = updated
            else:
                mimetype = mimetypes.guess_type(self.get_disk_path(item))[0]
                if mimetype is not None and "image" in mimetype:
                    images = images + 1
        if last_update is None:
            # the gallery is empty
            last_updateFmt = "Never"
        else:
            last_updateFmt = last_update.strftime("%x %X")
        return (collections, images, last_updateFmt)
        
    def get_collection_count(self):
        collections = 0
        for dir in self.dirs:
            if os.path.isdir(self.get_disk_path(dir)):
                collections = collections + 1
        return collections
        
    def get_collections(self):
        collections = []
        for dir in self.dirs:
            if os.path.isdir(self.get_disk_path(dir)):
                collections.append({
                    'name': dir,
                    'num_images': self.get_image_count(dir),
                    'cover_thumb': self.get_cover_thumbnail(dir),
                    'last_update_fmt': datetime.datetime.fromtimestamp(os.path.getmtime(self.get_disk_path(dir))).strftime("%x %X")
                    })
        return collections
    
    def get_gallery_cover_thumbnail(self):
        cover_thumb = ""
        for dir in self.dirs:
            if os.path.isdir(self.get_disk_path(dir)):
                cover_thumb = self.get_cover_thumbnail(dir)
            if len(cover_thumb) > 0:
                return cover_thumb
        return cover_thumb
        
    def get_cover_thumbnail(self, dir):
        files = os.listdir(self.get_disk_path(dir))
        cover_thumb = ""
        for file in files:
            if not os.path.isdir(self.get_disk_path(dir, file)):
                if "cover" in file and os.path.exists(self.get_disk_path(dir, file, for_thumbs=True)):
                    if "image" in mimetypes.guess_type(self.get_disk_path(dir, file, for_thumbs=True))[0]:
                        cover_thumb = self.get_disk_path(dir, file, for_disk=False, for_thumbs=True)
                elif len(cover_thumb) == 0 and os.path.exists(self.get_disk_path(dir, file, for_thumbs=True)):
                    if "image" in mimetypes.guess_type(self.get_disk_path(dir, file, for_thumbs=True))[0]:
                        cover_thumb = self.get_disk_path(dir, file, for_disk=False, for_thumbs=True)
        return cover_thumb
        
    def get_image_count(self, dir):
        # get_images is pretty involved... do it simpler (though this is more difficult to maintain)
        images = 0
        files = os.listdir(self.get_disk_path(dir))
        for file in files:
            if not os.path.isdir(self.get_disk_path(dir, file)):
                images = images + 1
            else:
                images = images + self.get_image_count("%s/%s" % (dir, file))
        return images

    def get_images(self, dir):
        images = []
        try:
            files = os.listdir(self.get_disk_path(dir))
            files.sort()
            for file in files:
                if not os.path.isdir(self.get_disk_path(dir, file)):
                    if "image" in mimetypes.guess_type(self.get_disk_path(dir, file))[0]:
                        if not os.path.exists(self.get_disk_path(dir, for_thumbs=True)):
                            os.makedirs(self.get_disk_path(dir, for_thumbs=True))
                        if not os.path.exists(self.get_disk_path(dir, file, for_thumbs=True)):
                            source_image = PythonMagick.Image(self.get_disk_path(dir, file).encode("ascii", "ignore"))
                            source_image.transform("%s" % THUMB_WIDTH)
                            source_image.write(self.get_disk_path(dir, file, for_thumbs=True).encode("ascii", "ignore"))
                        images.append({
                            'name': file, 
                            'image': self.get_disk_path(dir, file, for_disk=False),
                            'thumb': self.get_disk_path(dir, file, for_disk=False, for_thumbs=True),
                            'type': mimetypes.guess_type(self.get_disk_path(dir, file))[0]
                            })
        except:
            raise
        return images

    def get_previous_image(self, dir, current_image=None):
        if current_image is None:
            return None
        set_next = False
        try:
            files = os.listdir(self.get_disk_path(dir))
            files.sort()
            files.reverse()
            for file in files:
                if not os.path.isdir(self.get_disk_path(dir, file)):
                    if "image" in mimetypes.guess_type(self.get_disk_path(dir, file))[0]:
                        if set_next is True:
                            return file
                        else:
                            set_next = (current_image == file)
        except:
            pass
        return None
                                        
    def get_next_image(self, dir, current_image=None):
        set_next = (current_image is None)
        try:
            files = os.listdir(self.get_disk_path(dir))
            files.sort()
            for file in files:
                if not os.path.isdir(self.get_disk_path(dir, file)):
                    if "image" in mimetypes.guess_type(self.get_disk_path(dir, file))[0]:
                        if set_next is True:
                            return file
                        else:
                            if current_image == file:
                                set_next = True
        except:
            pass
        return None

