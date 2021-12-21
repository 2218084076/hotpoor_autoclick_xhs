import tornado.ioloop
import tornado.web
import os
from AddHandler import PageAddAPIHandler
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/add",PageAddAPIHandler),
])

if __name__ == "__main__":
    tornado.options.define("port", default=8201, help="Run server on a specific port", type=int)
    tornado.options.parse_command_line()

    i18n_path = os.path.join(os.path.dirname(__file__), "locales")
    # tornado.locale.load_gettext_translations(i18n_path, 'en_US')
    tornado.locale.load_translations(i18n_path)
    tornado.locale.set_default_locale('zh_CN')

    application_server = tornado.httpserver.HTTPServer(application, xheaders=True)
    application_server.listen(8201)
    application_server.start()
    tornado.ioloop.IOLoop.instance().start()