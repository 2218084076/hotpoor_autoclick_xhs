from selenium import webdriver
import time
import xlwt
driver = webdriver.Chrome('C:/Users/LENOVO/anaconda3/Scripts/chromedriver.exe')
url = [
    "http://xhslink.com/c7nxne",
    "http://xhslink.com/P0vjoe",
    "http://xhslink.com/hiLkoe",
    "http://xhslink.com/Ycnwoe",
    "http://xhslink.com/NOnwoe",
    "http://xhslink.com/mgexoe",
    "http://xhslink.com/J7gxoe"
]
excel = xlwt.Workbook(encoding='utf-8',style_compression=0)
table = excel.add_sheet('1',cell_overwrite_ok=True)

n=1
for u in url:
    driver.get(f"{u}")
    time.sleep(3)
    user_name = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div[2]/h6')
    table.write(n,1,user_name.text)
    print(user_name.text)
    title = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/main/div')
    table.write(n,2,title.text)
    print(title.text)
    date = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[4]/div/span')
    table.write(n,3,date.text)
    print(date.text,'\n')
    n=n+1
    excel.save("D:/terry/阡.xls")
time.sleep(2)
driver.close()