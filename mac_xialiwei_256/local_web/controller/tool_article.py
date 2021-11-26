#!/bin/env python
#coding=utf-8
import os
import requests
import time
import tornado
import tornado.web
import tornado.gen
import tornado.httpclient
import tornado.escape
from tornado.escape import json_encode, json_decode
import urllib
import urllib.request
from random import randrange
import sys
from selenium import webdriver
import time
import random
import cv2
import numpy as np
import base64

# def add_alpha_channel(img):
#     """ 为jpg图像添加alpha通道 """
 
#     b_channel, g_channel, r_channel = cv2.split(img) # 剥离jpg图像通道
#     alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255 # 创建Alpha通道
 
#     img_new = cv2.merge((b_channel, g_channel, r_channel, alpha_channel)) # 融合通道
#     return img_new

# def merge_img(jpg_img, png_img, y1, y2, x1, x2):
#     """ 将png透明图像与jpg图像叠加 
#         y1,y2,x1,x2为叠加位置坐标值
#     """
    
#     # 判断jpg图像是否已经为4通道
#     if jpg_img.shape[2] == 3:
#         jpg_img = add_alpha_channel(jpg_img)
    
#     '''
#     当叠加图像时，可能因为叠加位置设置不当，导致png图像的边界超过背景jpg图像，而程序报错
#     这里设定一系列叠加位置的限制，可以满足png图像超出jpg图像范围时，依然可以正常叠加
#     '''
#     yy1 = 0
#     yy2 = png_img.shape[0]
#     xx1 = 0
#     xx2 = png_img.shape[1]
 
#     if x1 < 0:
#         xx1 = -x1
#         x1 = 0
#     if y1 < 0:
#         yy1 = - y1
#         y1 = 0
#     if x2 > jpg_img.shape[1]:
#         xx2 = png_img.shape[1] - (x2 - jpg_img.shape[1])
#         x2 = jpg_img.shape[1]
#     if y2 > jpg_img.shape[0]:
#         yy2 = png_img.shape[0] - (y2 - jpg_img.shape[0])
#         y2 = jpg_img.shape[0]
 
#     # 获取要覆盖图像的alpha值，将像素值除以255，使值保持在0-1之间
#     alpha_png = png_img[yy1:yy2,xx1:xx2,3] / 255.0
#     alpha_jpg = 1 - alpha_png
    
#     # 开始叠加
#     for c in range(0,3):
#         jpg_img[y1:y2, x1:x2, c] = ((alpha_jpg*jpg_img[y1:y2,x1:x2,c]) + (alpha_png*png_img[yy1:yy2,xx1:xx2,c]))
 
#     return jpg_img

@tornado.gen.coroutine
def get_article_info(short_link):
    # short_link = argv_dir.get("--link",None)
    print("\nshort_link:\t",short_link)
    browser = webdriver.Chrome()
    browser.get(short_link)
    browser.minimize_window()
    time.sleep(3)
    small_pic = browser.find_element_by_class_name("small-pic")
    div_i_imgs = small_pic.find_elements_by_tag_name("i")
    num = 0
    image_links = []
    # t = int(round(time.time() * 1000))  # 毫秒级时间戳
    t = browser.current_url.split("/")[5].split("?")[0]
    t_is_exists = os.path.exists(os.path.join(os.path.dirname(__file__),'../static/files/%s.%s'%(t,"json")))

    if not t_is_exists:

        headimgurl_parent = browser.find_element_by_class_name("author-item")
        headimgurl = headimgurl_parent.find_element_by_class_name("author-info").find_element_by_class_name("left-img").find_elements_by_tag_name("img")[0].get_attribute("src")
        aim_url = headimgurl
        print('\n',aim_url)
        aim_response = requests.get(aim_url)
        f = open(os.path.join(os.path.dirname(__file__),'../static/upload/%s_%s.%s'%(t,"head","jpg")), "ab")
        f.write(aim_response.content)  # 多媒体存储content
        f.close()


        img_jpg_path = os.path.join(os.path.dirname(__file__),'../static/upload/%s_%s.%s'%(t,"head","jpg"))
        img_png_path = os.path.join(os.path.dirname(__file__),'../static/img/xhs_head_cover.png')
     
        # 读取图像
        img_jpg = cv2.imread(img_jpg_path, cv2.IMREAD_UNCHANGED)
        img_png = cv2.imread(img_png_path, cv2.IMREAD_UNCHANGED)
        img_jpg = cv2.resize(img_jpg,(400,400))
        img_png = cv2.resize(img_png,(400,400))
     
        # 设置叠加位置坐标
        x1 = 0
        y1 = 0
        x2 = x1 + img_png.shape[1]
        y2 = y1 + img_png.shape[0]
     
        # 开始叠加
        # res_img = merge_img(img_jpg, img_png, y1, y2, x1, x2)
     
        # 显示结果图像
        # cv2.imshow('result', res_img)
     
        # 保存结果图像，读者可自行修改文件路径
        # cv2.imwrite(img_jpg_path, res_img)

        headimgurl = '/static/upload/%s_%s.%s'%(t,"head","jpg")
        username = browser.find_element_by_class_name("author-item").find_element_by_class_name("author-info").find_element_by_class_name("name").text
        for div_i_img in div_i_imgs:
            link ="https://%s?imageView2/2/w/1080/format/jpg"%(div_i_img.get_attribute("style").split("https://")[1].split("?imageView2/2/")[0])
            aim_url = link
            print('\naim_url\t',aim_url)
            aim_response = requests.get(aim_url)
            f = open(os.path.join(os.path.dirname(__file__),'../static/upload/%s_%s.%s'%(t,num,"jpg")), "ab")
            f.write(aim_response.content)  # 多媒体存储content
            f.close()
            image_links.append("/static/upload/%s_%s.%s"%(t,num,"jpg"))
            num +=1
        print(num)
        title = browser.find_element_by_class_name("title").text
        title = title + 'kuai团团'
        a = randrange(0,(len(title)-1))
        title = title.replace(title[a],'!唇釉💄口红!!',1)

        # content = browser.find_element_by_class_name("content").text
        content = '快团团!!国货界沧海遗珠!奶欲低饱和度氛围感美女速进‼质地丝滑!上嘴好推开!显色极高!不显唇纹!不拔干!小程序!!快团团 '
        
        a = random.randrange(0,len(content.split('!')))
        content = content.replace(content.split('!')[a], ' 💄慕斯唇泥直接封神‼ ', 1)
        browser.find_element_by_class_name("author-item").find_element_by_class_name("author-info").click()
        browser.minimize_window()
        time.sleep(3)
        browser.switch_to.window(browser.window_handles[1])
        user_xhs = browser.current_url.split("/user/profile/")[1]
        browser.minimize_window()
        result = {
            "short_link":short_link,
            "type":"news",
            "image_num":num,
            "title":title,
            "content":content,
            "image_links":image_links,
            "t":t,
            "user_headimgurl":headimgurl,
            "user_name":username,
            "user_xhs":user_xhs,
        }
        result_json = json_encode(result)
        f = open(os.path.join(os.path.dirname(__file__),'../static/files/%s.%s'%(t,"json")), "ab")
        f.write(result_json.encode())  # 多媒体存储content
        f.close()
    else:
        f = open(os.path.join(os.path.dirname(__file__),'../static/files/%s.%s'%(t,"json"))).read()
        result = json_decode(f)
    browser.quit()
    return result
class MakeVideoArticleAPIHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def post(self):
        imgs = json_decode(self.get_argument("imgs","[]"))
        t = self.get_argument("t",None)
        if not t:
            self.finish({"info":"error"})
            return
        num = 0
        img_remove_list = []
        for img in imgs:
            b64_data = img.split(';base64,')[1]
            data = base64.b64decode(b64_data)
            img_path = os.path.join(os.path.dirname(__file__),'../static/temp/%s_%s.%s'%(t,num,"png"))
            img_path_jpg = os.path.join(os.path.dirname(__file__),'../static/temp/%s_%s.%s'%(t,num,"jpg"))
            f = open(img_path, "ab")
            f.write(data)  # 多媒体存储content
            f.close()
            f_cv = cv2.imread(img_path)
            cv2.imwrite(img_path_jpg,f_cv)
            num +=1
            img_remove_list.append(img_path)
            img_remove_list.append(img_path_jpg)
        imgs_path = os.path.join(os.path.dirname(__file__),'../static/temp')
        video_path = os.path.join(os.path.dirname(__file__),'../static/temp')
        os.system("ffmpeg -y -r 0.5 -f image2 -i %s/%s_%%d.%s -vcodec libx264 %s/%s.mp4"%(imgs_path,t,"jpg",video_path,t))
        for img_path in img_remove_list:
            os.remove(img_path)
        self.finish({"info":"ok","video":"/static/temp/%s.mp4"%(t)})
        # print('====上传====')
        # os.system('adb push D:\github\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\temp\%s.mp4 /sdcard/DCIM/Camera'%(t))
        # time.sleep(4)
        # os.system('adb shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera/')
        # time.sleep(4)

class ArticleDemoHandler(tornado.web.RequestHandler):
    def get(self):
        self.time_now = int(time.time())
        self.render("../template/demo/article.html")

class GetArticleInfoAPIHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        short_link = self.get_argument("short_link",None)
        if not short_link:
            self.finish({"info":"error","about":"no short link"})
            return
        result = yield get_article_info(short_link)
        self.finish({"info":"ok","result":result})
class GetArticleJsonAPIHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        t = self.get_argument("t",None)
        if not t:
            self.finish({"info":"error","about":"no t"})
            return
        f = open(os.path.join(os.path.dirname(__file__),'../static/files/%s.%s'%(t,"json"))).read()
        result = json_decode(f)
        self.finish({"info":"ok","result":result})
