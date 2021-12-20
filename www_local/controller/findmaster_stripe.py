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
import nomagic.block
from nomagic.cache import get_user, get_users, update_user, get_doc, get_docs, update_doc, get_aim, get_aims, update_aim, get_entity, get_entities, update_entity
from nomagic.cache import BIG_CACHE
from setting import settings
from setting import conn

# from user_agents import parse as uaparse #早年KJ用来判断设备使用

from .base import WebRequest
from .base import WebSocket
import pymail

from .data import DataWebSocket

import stripe
class HoldProductCaptureAPIHandler(WebRequest):
    @tornado.gen.coroutine
    def get(self):
        payment_intent_id = self.get_argument("payment_intent_id",None)
        payment_capture = int(self.get_argument("amount_to_capture",50))
        stripe.api_key = "sk_test_51K10IEABJaSnqIjxhNl1hVos346IJ5avHIswcEz4Ga2nUFxJrXHxJeBBnarbTTG7jMQ8KTgurdo7uRQMlUyY1J8V007VHMN0R2"
        intent = stripe.PaymentIntent.capture(
          payment_intent_id,
          amount_to_capture=payment_capture
        )
        self.finish({"info":"ok","about":"",})


class HoldProductCancelAPIHandler(WebRequest):
    def get(self):
        pass
class HoldProductAPIHandler(WebRequest):
    @tornado.gen.coroutine
    def get(self):
        pay_type = self.get_argument("pay_type","test")
        
        stripe.api_key = "sk_test_51K10IEABJaSnqIjxhNl1hVos346IJ5avHIswcEz4Ga2nUFxJrXHxJeBBnarbTTG7jMQ8KTgurdo7uRQMlUyY1J8V007VHMN0R2"
        if pay_type in ["online"]:
            stripe.api_key = "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"
        currency = self.get_argument("currency","usd")
        name = self.get_argument("name","DEMO Product")
        unit_amount = int(self.get_argument("unit_amount",50))
        quantity = int(self.get_argument("quantity",1))
        amount = unit_amount*quantity

        # customer = stripe.Customer.create()


        payment_intent = stripe.PaymentIntent.create(
          amount=amount,
          currency=currency,
          # payment_method_types=['card'],
          # confirm=True,
          capture_method='manual'
        )
        print(payment_intent)
        self.finish({"info":"ok","about":"hold product","payment_intent":payment_intent})

        # session = stripe.checkout.Session.create(
        #     line_items=[{
        #         "price_data": {
        #             "currency": currency,
        #             "product_data": {
        #                 "name": name,
        #                 "images":[
        #                     "http://fm-of-test0.xialiwei.com/659388851e8a4b2989de2203035331ba_7ae4379427cb2c6b0d302f67aef6460c?imageView2",
        #                     "http://fm-of-test0.xialiwei.com/659388851e8a4b2989de2203035331ba_f5d3e059a14d0e25be0cac2cbf34d5d4?imageView2",
        #                 ]
        #             },
        #             'unit_amount': unit_amount,
        #         },
        #         'quantity': quantity,
        #     }],
        #     mode='payment',
        #     success_url='https://findmaster.xialiwei.com/api/stripe/pay_success',
        #     cancel_url='https://findmaster.xialiwei.com/api/stripe/pay_cancel',
        # )
        # self.finish({"info":"ok","about":"pay product","redirect_uri":session.url})
class PayProductAPIHandler(WebRequest):
    def get(self):
        pay_type = self.get_argument("pay_type","test")
        
        stripe.api_key = "sk_test_51K10IEABJaSnqIjxhNl1hVos346IJ5avHIswcEz4Ga2nUFxJrXHxJeBBnarbTTG7jMQ8KTgurdo7uRQMlUyY1J8V007VHMN0R2"
        if pay_type in ["online"]:
            stripe.api_key = "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"
        currency = self.get_argument("currency","usd")
        name = self.get_argument("name","DEMO Product")
        unit_amount = int(self.get_argument("unit_amount",50))
        quantity = int(self.get_argument("quantity",1))

        session = stripe.checkout.Session.create(
            line_items=[{
                "price_data": {
                    "currency": currency,
                    "product_data": {
                        "name": name,
                        "images":[
                            "http://fm-of-test0.xialiwei.com/659388851e8a4b2989de2203035331ba_7ae4379427cb2c6b0d302f67aef6460c?imageView2",
                            "http://fm-of-test0.xialiwei.com/659388851e8a4b2989de2203035331ba_f5d3e059a14d0e25be0cac2cbf34d5d4?imageView2",
                        ]
                    },
                    'unit_amount': unit_amount,
                },
                'quantity': quantity,
            }],
            mode='payment',
            success_url='https://findmaster.xialiwei.com/api/stripe/pay_success',
            cancel_url='https://findmaster.xialiwei.com/api/stripe/pay_cancel',
        )
        self.finish({"info":"ok","about":"pay product","redirect_uri":session.url})
class PaySuccessAPIHandler(WebRequest):
    def get(self):
        self.finish({"info":"ok","about":"pay success"})
class PayCancelAPIHandler(WebRequest):
    def get(self):
        self.finish({"info":"ok","about":"pay cancel"})

latest_request_body = None
class WebhookAPIHandler(WebRequest):
    def post(self):
        print("webhook")
        global latest_request_body
        latest_request_body = json_decode(self.request.body)
        print(latest_request_body)
        self.finish({"info":"ok"})
class LatestWebhookAPIHandler(WebRequest):
    def get(self):
        print(latest_request_body)
        self.finish({"info":"ok","about":"latest request body","data":latest_request_body})









