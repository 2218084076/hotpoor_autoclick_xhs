import pyautogui
import pyperclip
from time import sleep

'''
ids=[]
cards=document.getElementsByClassName("daren-card")
for(i=0;i<cards.length;i++){
ids.push(cards[i].dataset["itemUid"])
}


'ids=[]\n'
'cards=document.getElementsByClassName("daren-card")\n'
'for(i=0;i<cards.length;i++){\n'
'if(cards[i].getElementsByTagName("div").length>30 && cards[i].getElementsByTagName("div")[30].textContent == "已邀约"){\n'
'console.log("0")}\n'
'else{\n'
'ids.push(cards[i].dataset["itemUid"])\n}}'

'''

def get_id():
    pyautogui.moveTo(x=1205,y=179,duration=0.3)
    pyautogui.click(x=1205,y=179,button='left')
    pyautogui.moveTo(x=1205,y=179,duration=0.3)
    pyautogui.click(x=1205,y=179,button='left')

    pyautogui.moveTo(x=1308,y=682,duration=0.3)
    pyautogui.click(x=1308,y=682,button='left')

    pyperclip.copy('ids=[]\n'
                   'cards=document.getElementsByClassName("daren-card")\n'
                   'for(i=0;i<cards.length;i++){\nids.push(cards[i].dataset["itemUid"])\n'
                   '}')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.keyDown('enter')

    pyautogui.moveTo(x=1205,y=179,duration=0.3)
    pyautogui.click(x=1205,y=179,button='left')

    pyautogui.moveTo(x=1308,y=682,duration=0.3)
    pyautogui.click(x=1308,y=682,button='left')

    pyperclip.copy('ids')
    pyautogui.hotkey('ctrl','v')
    pyautogui.keyDown('enter')

    pyautogui.moveTo(x=1702,y=254,duration=0.3)
    pyautogui.click(x=1702,y=254,button='left')
    pyautogui.doubleClick(x=1702,y=254)
    pyautogui.doubleClick(x=1702,y=254)
    pyautogui.hotkey('ctrl','c')
    sleep(2)
    pyautogui.moveTo(x=959,y=1048,duration=0.3)
    pyautogui.click(x=959,y=1048,button='left')

    # pyautogui.moveTo(x=1111,y=445, duration=0.3)
    # pyautogui.click(x=1111,y=445, button='left')

    pyautogui.hotkey('ctrl','v')
    pyautogui.keyDown('enter')

    pyautogui.moveTo(x=1010,y=1054, duration=0.3)
    pyautogui.click(x=1010,y=1054, button='left')
    sleep(2)
    pyautogui.moveTo(x=1085,y=964, duration=0.3)
    pyautogui.click(x=1085,y=964, button='left')
    sleep(2)

for n in range(1,31):
    get_id()
    print(n)
