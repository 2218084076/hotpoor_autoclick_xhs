#!/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import os.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/vendor/')
import re
import uuid
import time
import random
import string
import hashlib
import urllib
import copy
from functools import partial
import logging
import datetime
import markdown
import tornado
import tornado.web
import tornado.escape
import tornado.websocket
import tornado.httpclient
import tornado.gen
from tornado.escape import json_encode, json_decode
import nomagic

import nomagic.auth
# import nomagic.testblock
from nomagic.cache import get_user, get_users, update_user, get_doc, get_docs, update_doc, get_aim, get_aims, update_aim, get_entity, get_entities, update_entity
from nomagic.cache import BIG_CACHE
from setting import settings
from setting import conn
# from user_agents import parse as uaparse #早年KJ用来判断设备使用
from .base import WebRequest
from .base import WebSocket
import pymail


class CreatTestBlockAPIHandler(WebRequest):
    @tornado.gen.coroutine
    def get(self):
        block = {
            'owner': None,
            'packages': [],
        }
        [block_id, block] = nomagic.testblock.create_block(block)
        for i in range(10):
            block["packages"].append(i)
        update_aim(block_id, block)
        self.finish({'info': 'aready created inserted', 'id': block_id})


class UpdateTestBlockAPIHandler(WebRequest):
    @tornado.gen.coroutine
    def get(self):
        block_id = self.get_argument('block_id', None)
        if not block_id:
            self.finish({'info': 'no block id'})
            return
        block = get_aim(block_id)
        if not block:
            self.finish({'info': 'no block'})
            return
        for i in range(10):
            block["packages"].append(i)
        update_aim(block_id, block)
        self.finish({'info': 'aready updated', 'id': block_id})


class GetTestBlockAPIHandler(WebRequest):
    @tornado.gen.coroutine
    def get(self):
        block_id = self.get_argument('block_id', None)
        if not block_id:
            self.finish({'info': 'no block id'})
            return
        block = get_aim(block_id)
        if not block:
            self.finish({'info': 'no block'})
            return
        self.finish({'info': "ok", 'data': block})