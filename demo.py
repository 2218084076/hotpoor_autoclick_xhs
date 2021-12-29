from selenium import webdriver
from time import sleep
import xlwt

excel = xlwt.Workbook(encoding='utf-8',style_compression=0)
table = excel.add_sheet('1',cell_overwrite_ok=True)
d = webdriver.Chrome()
d.get('https://s.taobao.com/search?q=pinkbear%E9%95%9C%E9%9D%A2%E5%94%87%E9%87%89&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc')
sleep(10)
a=d.find_elements_by_class_name('deal-cnt')
for i in range(0,len(a)):

    table.write(i,1,a[i].text)
    excel.save("C:/Users/Terry/Desktop/1.xls")
    print(a[i].text)
    # sleep(0.5)
d.quit()