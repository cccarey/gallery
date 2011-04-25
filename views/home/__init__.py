import web, config
import os

from app.gallery import Gallery

session = web.config._session
render = config.render

class root:
    def GET(self):
        # 'test-pics' below needs to be from the user's galleries
        return render.home2(Gallery('test-pics'))
    
        """
        # 'test-pics' below needs to be from the user's galleries
        galleryDir = '%s/galleries/test-pics' % os.getcwd()
        iterDirs = os.listdir(galleryDir)
        dirs = []
        
        for dir in iterDirs:
            if os.path.isdir('%s/%s' % (galleryDir, dir)):
                dirs.append({'name': dir, 'files': os.listdir('%s/%s' % (galleryDir, dir))})
            else:
                dirs.append({'name': dir, 'files': []})
                
        return render.home(dirs)
        """