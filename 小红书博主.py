from selenium import webdriver
import time
import xlwt
import datetime
import random

excel = xlwt.Workbook(encoding='utf-8',style_compression=0)
table = excel.add_sheet('小红书博主及文章信息',cell_overwrite_ok=True)
driver = webdriver.Chrome()
url = '7 碎碎念的岁岁发布了一篇小红书笔记，快来看吧！ 😆 KjnkMxzYCYLZkxC 😆 http://xhslink.com/CbPuLe，复制本条信息，打开【小红书】App查看精彩内容！'
url = 'http'+url.split("http")[1].split(', 复制')[0]
driver.get(url)
driver.minimize_window()
time.sleep(4)
article_url = driver.current_url
print('作品链接：',article_url)
item_id = article_url.split('/item/')[1].split('?xhsshare')[0]
print('作品item_id',item_id)
title = driver.find_element_by_class_name('note-top').text
print('title：',title)
content = driver.find_element_by_class_name('content').text
table.write(1,2,content)
print('文案：\n',content)
name = driver.find_element_by_class_name('name').text
table.write(1,1,name)
print('博主名',name)
driver.find_element_by_class_name("author-item").find_element_by_class_name("author-info").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
user_url = driver.current_url
print('博主链接：',user_url)
user_id = user_url.split("/user/profile/")[1]
print('user_id: ',user_id)
excel.save(f"D:/Desktop/小红书.xls")
driver.quit()