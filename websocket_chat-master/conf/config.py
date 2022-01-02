#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 创建时间：2020/5/19 0019 13:15
__author__ = 'xiaoxiaoming'

# Tornado app配置
import base64
import os
import uuid

settings = {
    'template_path': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'template'),
    'static_path': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static'),
    # "static_url_prefix": "/",
    'cookie_secret': base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes),
    'xsrf_cookies': False,
    'login_url': '/signin',
    'debug': True,
}
print(settings)
# 日志
log_path = os.path.join(os.path.dirname(__file__), 'logs/log')
