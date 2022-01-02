#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 创建时间：2020/5/17 0017 19:15
__author__ = 'xiaoxiaoming'

import base64
import json
import random
from typing import Optional

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler

from bot_util import chatting, textchat
from conf import config
import logging

from random_name import random_name

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s:%(name)s:%(filename)s:%(lineno)d行:%(levelname)s: %(message)s')

define("host", default="127.0.0.1", type=str)
define("port", default=8000, type=int, help="run server on the given port.")


def parseUser(r: Optional[str]) -> Optional[dict]:
    if r:
        return json.loads(base64.b64decode(r).decode("utf-8"))
    return None


class IndexHandler(RequestHandler):
    def get_current_user(self):
        """在此完成用户的认证逻辑"""
        user: dict = parseUser(self.get_secure_cookie("user"))
        return user

    @tornado.web.authenticated
    def get(self):
        current_user = self.current_user
        logging.info(f"当前登陆的用户：{current_user}")
        self.render("room.html", title="web聊天室", user=current_user, host=options.host, port=options.port)


class SigninHandler(RequestHandler):
    index = 0

    def get(self):
        self.render("signin.html", title="web聊天室", name=random_name(), user=None, maximgid=27,
                    random_img_id=random.randrange(27))

    def post(self):
        SigninHandler.index += 1
        logging.info(f"注册接口被调用，当前索引:{SigninHandler.index}")
        name = self.get_body_argument("name")
        imgid = self.get_body_argument("imgid")
        user = {
            "id": SigninHandler.index,
            "name": name,
            "imageid": imgid
        }
        logging.info(f"写入cookie的对象:{user}")
        value = base64.b64encode(json.dumps(user).encode("utf-8"))
        self.set_secure_cookie("user", value)
        self.redirect("/")


class SignoutHandler(RequestHandler):
    def get(self):
        self.clear_cookie('user')
        self.redirect('/signin')


bot_ = {
    "id": 0,
    "name": "机器人小小鸟",
    "imageid": "bot"
}


class ChatHandler(WebSocketHandler):
    users = set()  # 用来存放在线用户的容器
    user = None  # 当前用户
    users_json = [bot_]  # 准备发给客户端的用户列表数据
    messageIndex = 0

    def createMessage(self, type, user, data):
        ChatHandler.messageIndex += 1
        # print(self.messageIndex)
        message = {
            "id": ChatHandler.messageIndex,
            "type": type,
            "user": user,
            "data": data
        }
        logging.info(f"创建一条消息：{message}")
        return json.dumps(message)

    def open(self):
        self.user = parseUser(self.get_secure_cookie("user"))
        if self.user is None:
            self.close(4001, 'Invalid user')
            return
        logging.info(f"{self.user}连接了WebSocket服务端...")
        self.users.add(self)  # 建立连接后添加用户到容器中
        self.users_json.append(self.user)

        # message = self.createMessage('join', self.user, self.user)
        message = self.createMessage('join', self.user, f"{self.user['name']}进入了聊天室.")
        for u in self.users:  # 向已在线用户发送消息
            u.write_message(message)
        # 通知当前上线的用户，在线用户列表
        self.write_message(self.createMessage('list', self.user, self.users_json))

    def on_message(self, message):
        msg = self.createMessage('chat', self.user, message.strip())
        self.send_msg(msg)
        msg = textchat(message.strip())
        if msg:
            msg = self.createMessage('chat', bot_, msg)
            self.send_msg(msg)

    def send_msg(self, msg):
        for u in self.users:  # 向在线用户广播消息
            u.write_message(msg)

    def on_close(self):
        self.users.remove(self)  # 用户关闭连接后从容器中移除用户
        self.users_json.remove(self.user)
        msg = self.createMessage('left', self.user, f"{self.user['name']}离开了聊天室.")
        self.send_msg(msg)

    def check_origin(self, origin):
        logging.info(origin)  # http://192.168.40.1:9000
        return True  # 允许WebSocket的跨域请求


if __name__ == '__main__':
    tornado.options.parse_config_file("./conf/config.ini")
    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/signin", SigninHandler),
        (r"/signout", SignoutHandler),
        (r"/ws/chat", ChatHandler),
    ], **config.settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print(f"http://{options.host}:{options.port}/")
    tornado.ioloop.IOLoop.current().start()
