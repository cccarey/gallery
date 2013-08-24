import web

BASEDIR = '/..'

render = web.template.render('templates', globals={ 'basedir': BASEDIR })

IMAGE_PATHS = {
    'disk_root': '/var/www/gallery-pics',
    'http_root': 'http://localhost/gallery-pics',
    'galleries': 'galleries',
    'thumbs': 'thumbs'
}

THUMB_WIDTH = 125

DB = web.database(dbn="sqlite", db="images.db")

