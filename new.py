import pyautogui
import time
import json

id_list = []

url_list=[]
news_urls = []

print('url_list',len(id_list))
news_ids = []
for id in id_list:
    if id not in news_ids:
        news_ids.append(id)
print('news_ids:',len(news_ids))

url = 'https://buyin.jinritemai.com/dashboard/servicehall/daren-profile?uid='
for i in news_ids:
    user_url = url + i
    url_list.append(user_url)
num = 1

for n in range(4,100):
    if url_list[n] not in news_urls:
        news_urls.append(url_list[n])
        pyautogui.moveTo(x=617,y=74,duration=0.3)
        pyautogui.click(x=617,y=74,button='left')
        pyautogui.hotkey('ctrl','l')
        pyautogui.typewrite(f'{url_list[n]}')
        pyautogui.keyDown('enter')
        time.sleep(8)
        pyautogui.moveTo(x=1039,y=193,duration=0.3)
        pyautogui.click(x=1039,y=193, button='left')
        time.sleep(0.5)

        pyautogui.moveTo(x=1039,y=193,duration=0.3)
        pyautogui.click(x=1039,y=193,button='left')
        time.sleep(0.5)

        pyautogui.moveTo(x=1067,y=742,duration=0.3)
        pyautogui.click(x=1067,y=742,button='left')
        time.sleep(0.5)

        pyautogui.typewrite('document.getElementsByClassName("contact-btn")[0].click()')
        pyautogui.keyDown('enter')
        time.sleep(2)

        pyautogui.typewrite('document.getElementsByClassName("add-product-operate")[0].getElementsByTagName("button")[0].click()')
        pyautogui.keyDown('enter')
        time.sleep(0.5)

        pyautogui.moveTo(x=157,y=636,duration=0.3)
        pyautogui.click(x=157,y=636,button='left')
        time.sleep(0.5)


        pyautogui.moveTo(x=682,y=804,duration=0.3)
        pyautogui.click(x=682,y=804,button='left')
        time.sleep(0.5)

        # pyautogui.typewrite('document.getElementsByClassName("ant-checkbox")[0].getElementsByTagName("input")[0].click()')
        # pyautogui.keyDown('enter')
        # time.sleep(2)

        pyautogui.moveTo(x=790,y=973,duration=0.3)
        pyautogui.click(x=790,y=973,button='left')
        time.sleep(0.5)

        print(num)
        print(url_list[n])
        num+=1