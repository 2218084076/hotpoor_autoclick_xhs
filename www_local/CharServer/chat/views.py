# -*- coding: utf-8 -*-
import datetime
import json

import tornado.web
import tornado.websocket
from tornado.web import authenticated  # 导入装饰器
from pycket.session import SessionMixin


# 设置BaseHandler类，重写函数get_current_user
class BaseHandler(tornado.web.RequestHandler, SessionMixin):
    def get_current_user(self):  # 前面有绿色小圆圈带个o，再加一个箭头表示重写
        current_user = self.session.get('user')  # 获取加密的cookie
        if current_user:
            return current_user
        return None


# 基类
class BaseWebSocketHandler(tornado.websocket.WebSocketHandler, SessionMixin):
    def get_current_user(self):
        current_user = self.session.get('user')

        if current_user:
            return current_user
        return None


# 跳转
class IndexHandler(BaseHandler):
    @authenticated  # 内置装饰器,检查是否登录
    def get(self):
        self.render('chat.html')


class LoginHandler(BaseHandler):
    def get(self):
        self.render('index.html')  # 跳转页面带上获取的参数

    def post(self, *args, **kwargs):
        user = self.get_argument('nickname', '')
        if user:

            self.session.set('user', user)  # 设置加密cookie
            self.redirect('/')  # 跳转到之前的路由
        else:
            self.render('index.html')


class ChatHandler(BaseWebSocketHandler):
    # 定义接收/发送聊天消息的视图处理类，继承自websocket的WebSocketHandler
    # 定义一个集合，用来保存在线的所有用户

    online_users = set()

    # 从客户端获取cookie信息

    # 重写open方法，当有新的聊天用户进入的时候自动触发该函数
    def open(self):

        # 新用户上线,加入集合
        self.online_users.add(self)
        # 将新用户加入的信息发送给所有用户

        for user in self.online_users:
            user.write_message('[%s]join room' % self.current_user)

    # 重写on_message方法，当聊天消息有更新时自动触发的函数
    def on_message(self, message):
        msgobj = {'msg': message}

        for user in self.online_users:
            msgobj['key'] = '%s-%s-sea: ' % (self.current_user, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            user.write_message(json.dumps(msgobj))


    # 重写on_close方法，当有用户离开时自动触发的函数
    def on_close(self):
        # 移除用户
        self.online_users.remove(self)
        for user in self.online_users:
            user.write_message('[%s]remove room' % self.current_user)

    # 重写check_origin方法, 解决WebSocket的跨域请求
    def check_origin(self, origin):
        return True