import pyautogui
import time
import pyperclip
import json
# 921.6

url_list=[]
news_urls = []

def pyautogui_action(action):
    if action["name"] in ["move_to_click"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')

    elif action["name"] in ["select_all_and_copy"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "c")

    elif action["name"] in ["select_all_and_paste"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "v")

    elif action["name"] in ["select_all_and_copy_and_paste"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        write_content = action.get("content","")
        pyperclip.copy(write_content)
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press('enter')

    elif action["name"] in ["open_console"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("f12")
    print(action.get("action_name"))
    action_sleep = action.get("sleep",0)
    time.sleep(action_sleep)

for n in range(0,1):
    for i in range(0,20):
        pyautogui.moveTo(x=1209,y=178,duration=0.3)
        pyautogui.click(x=1209,y=178, button='left')
        pyautogui.moveTo(x=1209,y=178,duration=0.3)
        pyautogui.click(x=1209,y=178,button='left')
        pyautogui.moveTo(x=1324,y=819,duration=0.3)
        pyautogui.click(x=1324,y=819,button='left')
        pyperclip.copy('document.getElementsByClassName("daren-card")[%s].click()'%(i))
        pyautogui.hotkey('ctrl','v')
        pyautogui.keyDown('enter')
        time.sleep(5)
        pyautogui.moveTo(x=194,y=617,duration=0.3)
        pyautogui.click(x=194,y=617, button='left')

        pyautogui.moveTo(x=972,y=533,duration=0.3)
        pyautogui.click(x=972,y=533, button='left')

        pyautogui.moveTo(x=626,y=440,duration=0.3)
        pyautogui.click(x=626,y=440, button='left')

        pyautogui.moveTo(x=1162,y=906,duration=0.3)
        pyautogui.click(x=1162,y=906, button='left')

        pyautogui.moveTo(x=1723,y=976,duration=0.3)
        pyautogui.click(x=1723,y=976,button='left')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(0.5)
        print('document.getElementsByClassName("daren-card")[%s]'%(i))
    pyautogui.moveTo(x=1209, y=178, duration=0.3)
    pyautogui.click(x=1209, y=178, button='left')
    pyautogui.moveTo(x=1209, y=178, duration=0.3)
    pyautogui.click(x=1209, y=178, button='left')
    pyautogui.moveTo(x=1324, y=819, duration=0.3)
    pyautogui.click(x=1324, y=819, button='left')
    pyperclip.copy('document.getElementsByClassName("auxo-pagination-item-link")[2].click()')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.keyDown('enter')

    time.time(1)

'''
result=[]
result.push($(".daren-overview-base-nameblock").innerText)
result.push($(".daren-overview-base-traitblock").innerText)
result.push(document.getElementsByClassName("data-overview-dashboard-items-item__value")[0].innerText)
result.push(document.getElementsByClassName("data-overview-dashboard-items-item__value")[1].innerText)
result.push(document.getElementsByClassName("data-overview-dashboard-items-item__value")[2].innerText)
result.push(document.getElementsByClassName("data-overview-dashboard-items-item__value")[3].innerText)
result.push(document.getElementsByClassName("data-overview-dashboard-items-item__value")[4].innerText)
result.push(document.getElementsByClassName("data-overview-dashboard-items-item__value")[6].innerText)
result_info = {
    "name":result[0],
    "traitblock":result[1],
    "frequency":result[2],
    "days":result[3],
    "promote":result[4],
    "cooperation":result[5],
    "people":result[6],
    "sales":result[7],
}
'''