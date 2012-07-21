import web

BASEDIR = '/..'

render = web.template.render('templates', globals={ 'basedir': BASEDIR })

IMAGE_PATHS = {
    'galleries': 'static/galleries',
    'thumbs': 'static/thumbs'
}

thumb_width = 125
