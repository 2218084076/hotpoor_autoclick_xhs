import time

import pyautogui
import pyperclip

'''
document.getElementById("wlb_cover").remove()

document.body.append(dom)

dom=document.createElement("div")
dom.id="wlb_cover"
dom.style.position="fixed"
dom.style.top="0px"
dom.style.right="0px"
dom.style.zIndex=9999999999999999999
dom.innerHTML="<textarea id=\"wlb_cover_textarea\">"+u+"</textarea>"
'''

def get_urls():
    pyautogui.moveTo(x=1205,y=179,duration=0.3)
    pyautogui.click(x=1205,y=179,button='left')
    pyautogui.moveTo(x=1205,y=179,duration=0.3)
    pyautogui.click(x=1205,y=179,button='left')

    pyautogui.moveTo(x=1308,y=682,duration=0.3)
    pyautogui.click(x=1308,y=682,button='left')

    pyperclip.copy('scrollBy(0,99999)')
    pyautogui.hotkey('ctrl','v')
    pyautogui.keyDown('enter')

    pyperclip.copy('''
u=[]
pics=document.getElementsByClassName("pic")
for(i=0;i<pics.length;i++){
u.push(pics[i].getElementsByTagName("a")[0].getAttribute("href"))}
'''
                   )
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.keyDown('enter')
    time.sleep(0.5)

    pyperclip.copy('u')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.keyDown('enter')

    pyautogui.moveTo(x=1684,y=411,duration=0.3)
    pyautogui.click(x=1684,y=411,button='left')
    pyautogui.doubleClick(x=1684,y=411)
    pyautogui.doubleClick(x=1684,y=411)
    pyautogui.hotkey('ctrl','c')


    pyautogui.moveTo(x=962,y=1048, duration=0.3)
    pyautogui.click(x=962,y=1048, button='left')

    time.sleep(1)
    pyautogui.hotkey('ctrl','v')
    pyautogui.keyDown('enter')
    time.sleep(1)

    pyautogui.moveTo(x=1012,y=1058, duration=0.3)
    pyautogui.click(x=1012,y=1058, button='left')
    time.sleep(1)
    pyautogui.moveTo(x=850,y=1008, duration=0.3)
    pyautogui.click(x=850,y=1008, button='left')

    pyautogui.moveTo(x=798,y=690,duration=0.3)
    pyautogui.click(x=798,y=690,button='left')

    time.sleep(4)

for i in range(1):
    print(i)
    get_urls()