import web

BASEDIR = '/..'

render = web.template.render('templates', globals={ 'basedir': BASEDIR })

IMAGE_PATHS = {
    'galleries': 'static/galleries',
    'thumbs': 'static/thumbs'
}

THUMB_WIDTH = 125
