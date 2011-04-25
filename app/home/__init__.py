import web, config

session = web.config._session
render = config.render

class root:
    def GET(self):
        return render.home()