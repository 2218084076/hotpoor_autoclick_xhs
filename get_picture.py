import time
import os
import requests

def download_image(img_url):
    aim_url = img_url.split(".jpg")[0]+".jpg"
    print("download:", aim_url)
    aim_response = requests.get(aim_url)
    t = int(round(time.time() * 1000))  # 毫秒集
    f = open(os.path.join(os.path.dirname(__file__),'D:/github/1/hotpoor_autoclick_xhs/map/%s.%s' % (aim_url, "jpg")), "ab")
    f.write(aim_response.content)
    f.close()
download_image('https://p0.meituan.net/merchantpic/1c1fde98234ad9e471434d8efff2d17861211.jpg%401000w_1000h_0e_1l%7Cwatermark%3D0')

