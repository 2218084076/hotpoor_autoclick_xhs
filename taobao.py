from selenium import webdriver
import time
import xlwt
import xlrd
import datetime
import random

excel = xlwt.Workbook(encoding='utf-8',style_compression=0)
table = excel.add_sheet('小红书博主及文章信息',cell_overwrite_ok=True)
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.taobao.com/?spm=a1z02.1.1581860521.1.2qUVWK')
driver.find_element_by_xpath('//*[@id="q"]').send_keys('儿童玩具')
time.sleep(2)
driver.find_element_by_class_name('search-button').click()
print('扫码登陆')
time.sleep(20)
i=0

js = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)
time.sleep(4)
js = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)
print(i)
i+=1

a = driver.find_element_by_id('mainsrp-itemlist').find_element_by_class_name('items').find_elements_by_tag_name('div')
# [0].find_element_by_tag_name('a').get_attribute('href')
time.sleep(5)
print(len(a))
def get_url(tag_list):
    s = 1
    a = tag_list
    for n in range(0,len(a)+1):
        t = random.randint(5,20)
        url = a[n].find_element_by_tag_name('a').get_attribute('href')
        time.sleep(t)
        table.write(s,0,url)
        print(f'num{s}',url)
        excel.save(f"D:/Desktop/1.xls")
        s+=1
driver.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/ul/li[9]').click()
driver.quit()