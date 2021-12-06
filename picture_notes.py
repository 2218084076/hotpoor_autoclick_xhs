import requests
import json
from selenium import webdriver
import time
import os
import xlwt
driver = webdriver.Chrome()
excel = xlwt.Workbook(encoding='utf-8',style_compression=0)
url_img = 'https://www.qianshanghua.com/api/page/comment/load?chat_id=8e940b2524c843789d29278c8d2b8cdc&comment_id='
table = excel.add_sheet('1',cell_overwrite_ok=True)
url_list = ['http://xhslink.com/6mAmwe']
img_list = []
def download_image(img_url):
    aim_url = img_url
    print("download:", aim_url)
    aim_response = requests.get(aim_url)
    t = int(round(time.time() * 1000))  # 毫秒集
    f = open(os.path.join(os.path.dirname(__file__),'D:/images/%s.%s' % (time.time(), "jpg")), "ab")
    f.write(aim_response.content)
    f.close()
def get_lurl (url_img):
    a = requests.get(url_img)
    a = a.text
    b = json.loads(a)
    for comment in b["comments"]:
        c = comment[4]
        if "http://" in c:
            d = "http://" + c.split("，")[1].split("http://")[1]
            url_list.append(d)
    #解析json中的作品短链接
def get_img (url):
    url_list=url
    for u in url_list:
        print(u)
        driver.get(u)
        time.sleep(8)
        a1 = driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div[1]/div[1]/div[2]')
        b1 = a1.find_elements_by_tag_name("div")
        for b in b1:
            c1 = b.find_element_by_tag_name("i")
            url_img = c1.get_attribute("style").split("https://")[1].split("\"")[0].split("/2/w")[0]
            url_img = "http://"+url_img
            print(url_img)
            download_image(url_img)
def user_page (url):
    url_list = url
    for works_u in url_list:
        driver.get(works_u)
        time.sleep(6)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[1]/span').click()
# get_lurl(url_img)
# print(url_list)
get_img(url_list)
driver.quit()

