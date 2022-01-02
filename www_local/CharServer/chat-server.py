#coding=utf-8

import tornado.websocket
import tornado.web
import tornado.ioloop
import os
import datetime

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('templates/index.html')
        class WebHandler(tornado.websocket.WebSocketHandler):
            users =set()#存放在线用户
    def open(self, *args, **kwargs):
        self.users.add(self)#把建立连接后的用户添加到用户容器中
        for user in self.users: #向在线的用户发送进入消息
            user.write_message("[%s]-[%s]-进入聊天室"% (self.request.remote_ip,
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    def on_close(self):
        self.users.remove(self)# 用户关闭连接后从容器中移除用户

        for user in self.users:
            user.write_message("[%s]-[%s]-离开聊天室"% (self.request.remote_ip,
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def on_message(self, message):
        for user in self.users:#向在线用户发送聊天消息
            user.write_message("[%s]-[%s]-说：%s"% (self.request.remote_ip,
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), message))

    def check_origin(self, origin):

        return True# 允许WebSocket的跨域请求



BASE_DIR = os.path.dirname(__file__)

settings = {

'static_path':os.path.join(BASE_DIR,'static'),

"websocket_ping_interval":1,

"websocket_ping_timeout":10

}

app = tornado.web.Application([(r'/',IndexHandler),

(r'/chat',WebHandler)],

**settings)

app.listen(8009)

tornado.ioloop.IOLoop.instance().start()