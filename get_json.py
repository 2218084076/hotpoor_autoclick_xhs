import requests
import json
from selenium import webdriver
import time
import os
import xlwt

excel = xlwt.Workbook(encoding='utf-8',style_compression=0)
table = excel.add_sheet('1',cell_overwrite_ok=True)
table.write(0,1,"博主")
table.write(0,2,"作品内容")
table.write(0,3,"作品长连接")
table.write(0,4,"作品短链接")
table.write(0,5,"用户主页")
table.write(0,6,"头像")
table.write(0,7,"主页介绍")
url_now ="https://www.qianshanghua.com/api/page/comment/load?chat_id=9724fbedab6843fb934e67b618474b2d&comment_id="
url_img ="https://www.qianshanghua.com/api/page/comment/load?chat_id=8e940b2524c843789d29278c8d2b8cdc&comment_id="
a = requests.get(url_now)
a = a.text
b = json.loads(a)
url_list = []
for comment in b["comments"]:
    c = comment[4]
    if "http://" in c:
        d = "http://"+c.split("，")[1].split("http://")[1]
        url_list.append(d)
driver = webdriver.Chrome()
get_video_urls=[]
driver_pages=[]
img_user = []
user_urls = []
n=1
def get_video(video_url):
    aim_url = video_url
    print(n,"download:", aim_url)
    aim_response = requests.get(aim_url)
    t = int(round(time.time() * 1000))  # 毫秒集
    f = open(os.path.join(os.path.dirname(__file__),'D:/video/%s.%s' % (time.time(), "mp4")), "ab")
    f.write(aim_response.content)
    f.close()
for u in url_list:
    driver.get(u)
    time.sleep(4)
    current_url = driver.current_url
    current_url = current_url.split("?")[0]

    table.write(n,3,current_url)
    table.write(n,4,u)
    name = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div[2]/h6')
    table.write(n,1,name.text)
    content = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/main/div')
    table.write(n,2,content.text)

    if current_url in driver_pages:
        continue
    driver_pages.append(current_url)

    scr = driver.find_element_by_tag_name("video")
    video = scr.get_attribute("src")
    # get_video(video)
#点击博主主页
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[1]/span').click()
    w = driver.window_handles
    driver.switch_to.window(w[n])
    user_url = driver.current_url
    table.write(n,5,user_url)
    im = driver.find_element_by_css_selector('#app > div > div.user-container.pc-container > div.author-card > div > div.left > div > div > div > img').get_attribute("src")
    table.write(n,6,im)
    cn = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div[2]')
    table.write(n,7,cn.text)
    n=n+1
    excel.save(f"D:/Desktop/阡.xls")
driver.quit()

