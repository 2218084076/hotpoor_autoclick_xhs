import tornado.ioloop
import tornado.web
import os
import json
import tornado.websocket

l=[]

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class GetIdHandler(tornado.web.RequestHandler):
    def get(self):
        txt = open("id_list.json",'r')
        for i in txt:
            l.append(i)
        self.write(json.dumps(l))

def make_app():
    return tornado.web.Application([
        (r"/id", GetIdHandler),
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()