import pyautogui
import time
import xlwt
import json

excel = xlwt.Workbook(encoding='utf-8',style_compression=0)
table = excel.add_sheet('1',cell_overwrite_ok=True)

file = 'doudian_user_ids.json'
id_list = ["f1ead985dbee25337c9f8988708ba0d8","26a40661c78c4acd07c77279173138f4","3cb5df6fcb466b7a55bc2ad62d7b2eb9","a2bbf56406e7ccd9223deebd38525598","59892258e18be7576a08fcb4862dcb69","0dd1c569d814cc51d313b041421b4acb","0b920a6b62244f55dacba75a2e151c0e","c2aa013015f268f6fc87da6f952193ac","3845dcd4e5b1a3c9c6082c395b92a530","94a6e5e9e2004cbc6388fe4f6ad3a6bd","9bff94be0ab8a17225a215da11361a2d","254c33a9c598d0701cb679bd22426cb4"
,"6158a373579205ddda7a80ff35fe1252","907ba6492487acc21891c67ff03bacfe","01d26da413997a87f1c872adfaab3fc0","9a4663cea1be74e0463a9423ce08e502","7f3061aa4482ebf6aed642ecb0bfbae4","9fef5aa58a7461af84e243970d30ce3f","51b85c1fbc194839929eca9d7edd07ce","b070a2cb9f902c8dc94f0952dd654a8c","180af50f45bd64f282944ab9953b0e86","d1114a4d6a876224cffd984b087c7ba7","d69489c40655a79dec2aa77a01f269df","1a9674167903421d5fae653c3f920869","977d965deab7fc14937299f75a1793a4","de829ffff2009546861397a9f69f15fd","485a7c7e727d155e9b5b49f90635443d","200bf1fe419d08889366ac84355bdecf","18568e2b5873f1f7d5eb78b2a393b887","0928f310c30832c2aece0eac781f0d3b","94f5448119655c77c173131ff014506f","0eb681de6710c3a2340402b88ca9b325"]
url_list=[]
news_urls = []
print(len(id_list))
news_ids = []
for id in id_list:
    if id not in news_ids:
        news_ids.append(id)
print(len(news_ids))

url = 'https://buyin.jinritemai.com/dashboard/servicehall/daren-profile?uid='
for i in news_ids:
    user_url = url + i
    url_list.append(user_url)
num = 1
for n in range(11,100):
    if url_list[n] not in news_urls:
        news_urls.append(url_list[n])
        pyautogui.moveTo(x=833,y=62,duration=0.5)
        pyautogui.click(x=833,y=62,button='left')
        pyautogui.hotkey('ctrl','l')
        print(url_list[n])
        pyautogui.typewrite(f'{url_list[n]}')
        pyautogui.keyDown('enter')
        time.sleep(10)
        # pyautogui.hotkey('f5')
        time.sleep(3)
        pyautogui.moveTo(x=1145,y=253,duration=0.5)
        pyautogui.click(x=1145,y=253, button='left')
        time.sleep(2)

        pyautogui.moveTo(x=1145,y=253,duration=0.5)
        pyautogui.click(x=1145,y=253, button='left')
        time.sleep(0.5)

        pyautogui.moveTo(x=1388,y=519,duration=0.5)
        pyautogui.click(x=1388,y=519, button='left')
        time.sleep(0.5)

        pyautogui.typewrite('document.getElementsByClassName("contact-btn")[0].click()')
        pyautogui.keyDown('enter')
        time.sleep(2)

        pyautogui.moveTo(x=314,y=535,duration=0.5)
        pyautogui.click(x=314,y=535, button='left')
        time.sleep(0.5)

        pyautogui.moveTo(x=216,y=618,duration=0.5)
        pyautogui.click(x=216,y=618, button='left')
        time.sleep(0.5)

        pyautogui.moveTo(x=750,y=787,duration=0.5)
        pyautogui.click(x=750,y=787,button='left')
        time.sleep(0.5)

        pyautogui.moveTo(x=890,y=986,duration=0.5)
        pyautogui.click(x=890,y=986,button='left')
        time.sleep(3)
        table.write(n,1,url_list[n])
        print(num)
        num+=1
        excel.save("C:/Users/Terry/Desktop/1.xls")
        print(len(news_urls))