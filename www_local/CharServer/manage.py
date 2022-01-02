import tornado.web
import tornado.httpserver
from tornado.options import define, options, parse_command_line

from chat.views import IndexHandler, LoginHandler, ChatHandler
from util.settings import TEMPLATE_PATH, STATIC_PATH

define("port", default=8180, help='run on the port', type=int)

def make_app():
    return tornado.web.Application(handlers=[
        (r'/', IndexHandler),
        (r'/login', LoginHandler),
        (r'/chat', ChatHandler),
    ],
        pycket={
            'engine': 'redis',
            'storage': {
                'host': 'fot.redis.cache.net',
                'port': 6379,
                'password': 'yKigE3ZF0mGBSP4/M=',
                'db_sessions': 5,
                'db_notifications': 11,
                'max_connections': 2 ** 31,
            },
            'cookies': {
                'expires_days': 30,
                'max_age': 100
            },
        },
        login_url='/login',
        template_path=TEMPLATE_PATH,
        static_path=STATIC_PATH,
        debug=True,
        cookie_secret='cqVJzSSjQgWzKtpHMd4NaSeEa6yTy0qRicyeUDIMSjo='
    )


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()