#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

import hashlib
import random
import time
from urllib import parse

import requests

from conf.config import app_id, app_key

nonce_max = 16 ** 30


def get_nonce_str():
    '获取随机字符串，用于保证签名不可预测'
    return hex(random.randrange(nonce_max))[2:]


def get_textchat_params(question) -> dict:
    params = {
        'app_id': app_id,
        'time_stamp': str(int(time.time())),
        'nonce_str': get_nonce_str(),
        'session': '10000',
        'question': question,
    }
    sign = gen_sign_string(params.items())
    params["sign"] = sign
    return params


def gen_sign_string(params) -> str:
    p = list(sorted(params))
    p.append(('app_key', app_key))
    sign_str = parse.urlencode(p)
    # 对字符串sign_before进行MD5运算，得到接口请求签名
    sign = hashlib.md5(sign_str.encode('UTF-8')).hexdigest().upper()
    return sign


# 聊天的API地址
textchat_url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"


def textchat(question):
    params = get_textchat_params(question.encode('utf-8'))
    r = requests.post(textchat_url, params)
    json = r.json()
    return json['data']['answer']


def chatting(content):
    for i in range(3):
        result = textchat(content)
        if result != "":
            return result
        time.sleep(0.1)
    return ""


if __name__ == '__main__':
    while True:
        question = input('我：')
        if question == 'q':
            break
        answer = chatting(question)
        print('机器人：', answer)
