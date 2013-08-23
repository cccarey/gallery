#!/usr/bin/env python
import sys, os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)

# following line lets web.seeother work so it does not include the 
# name of this file
os.environ['REAL_SCRIPT_NAME'] = ''

import web

URLS = (
    '/', 'views.home.root',
    '/gallery/(.+)', 'views.gallery.root',
    '/api/image/metadata/(.+)', 'api.image.metadata'
)

web_app = web.application(URLS, globals())
    
if __name__ == "__main__": 
    web_app.run()

application = web_app.wsgifunc()

