import pyautogui
import pyperclip
import time

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

def pyautogui_action(action):
    if action["name"] in ["move_to_click"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
    elif action["name"] in ["select_all_and_write"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        time.sleep(1)
        pyautogui.hotkey("ctrl", "a")
        write_content = action.get("content","")
        pyautogui.typewrite(write_content)
        pyautogui.press('enter')
    elif action["name"] in ["select_all_and_js_latest"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press('backspace')
        pyautogui.press('up')
        pyautogui.press('enter')
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
    elif action["name"] in ["select_item_and_close_tab"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "w")
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
    elif action["name"] in ["esc"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("esc")
    print(action.get("action_name"))
    action_sleep = action.get("sleep",0)
    time.sleep(action_sleep)

def get_id():
    pyautogui.moveTo(x=1205,y=179,duration=0.3)
    pyautogui.click(x=1205,y=179,button='left')
    pyautogui.moveTo(x=1205,y=179,duration=0.3)
    pyautogui.click(x=1205,y=179,button='left')

    pyautogui.moveTo(x=1308,y=682,duration=0.3)
    pyautogui.click(x=1308,y=682,button='left')

    pyperclip.copy('''
ids=[]cards=document.getElementsByClassName("daren-card")
for(i=0;i<cards.length;i++){
    ids.push(cards[i].dataset["itemUid"])
}
''')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.keyDown('enter')

while True:
    for p in range(0,20):
        action_item_click_list = [
            {
                "x":1377,
                "y":147,
                "sleep":0.5,
                "name":"move_to_click",
                "content":"",
                "action_name":"切换console",
            },
            {
                "x":1204,
                "y":172,
                "sleep":0.5,
                "name":"move_to_click",
                "content":"",
                "action_name":"清空信息console",
            },
            {
                "x": 1282,
                "y": 995,
                "sleep": 2,
                "name": "select_all_and_copy_and_paste",
                "content": '',
                "action_name": "切换产品",
            },
        ]