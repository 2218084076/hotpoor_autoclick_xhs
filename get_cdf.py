import sys
import os
import pyautogui
import time
import pyperclip
# Chrome打开浏览器 https://pgy.xiaohongshu.com/solar/advertiser/patterns/kol
# 选择分类
# 打开审查元素工具 位置1160px
# 滚动屏幕至全部右下角
page_num = 0
page_num_end = 3

page_with_items = [20,20,20]
action_list = [
    {
        "x":235,
        "y":47,
        "sleep":1,
        "name":"move_to_click",
        "content":"",
        "action_name":"切换pgy页面",
    },
]
def pyautogui_action(action):
    if action["name"] in ["move_to_click"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
    elif action["name"] in ["select_all_and_write"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        time.sleep(1)
        pyautogui.hotkey("command", "a")
        write_content = action.get("content","")
        pyautogui.typewrite(write_content)
        pyautogui.press('enter')
    elif action["name"] in ["select_all_and_js_latest"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("command", "a")
        pyautogui.press('backspace')
        pyautogui.press('up')
        pyautogui.press('enter')
    elif action["name"] in ["select_all_and_copy"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("command", "a")
        pyautogui.hotkey("command", "c")
    elif action["name"] in ["select_all_and_paste"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("command", "a")
        pyautogui.hotkey("command", "v")
    elif action["name"] in ["select_item_and_close_tab"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("command", "w")
    elif action["name"] in ["select_all_and_copy_and_paste"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        write_content = action.get("content","")
        pyperclip.copy(write_content)
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("command", "v")
        pyautogui.press('enter')
    print(action.get("action_name"))
    action_sleep = action.get("sleep",0)
    time.sleep(action_sleep)

for page in page_with_items:
    action_page_change = {
        "x":900,
        "y":47,
        "sleep":1,
        "name":"move_to_click",
        "content":"",
        "action_name":"点击选项卡",
    
    }
    pyautogui_action(action_page_change)
    for item in range(0,page):
        action_item_click_list = [
            {
                "x":1338,
                "y":147,
                "sleep":1,
                "name":"move_to_click",
                "content":"",
                "action_name":"切换console",
            },
            {
                "x":1206,
                "y":172,
                "sleep":1,
                "name":"move_to_click",
                "content":"",
                "action_name":"清空信息console",
            },
            {
                "x":1275,
                "y":197,
                "sleep":5,
                "name":"select_all_and_copy_and_paste",
                "content":"document.getElementsByClassName(\"product-item-default\")[%s].children[1].click()"%(item),
                "action_name":"切换产品",
            },
            {
                "x":1210,
                "y":49,
                "sleep":2,
                "name":"select_item_and_close_tab",
                "content":"",
                "action_name":"关闭选项卡",
            }
        ]
        for action_item_click in action_item_click_list:
            pyautogui_action(action_item_click)
    action_page_change_list = [
            {
                "x":1338,
                "y":147,
                "sleep":1,
                "name":"move_to_click",
                "content":"",
                "action_name":"切换console",
            },
            {
                "x":1206,
                "y":172,
                "sleep":1,
                "name":"move_to_click",
                "content":"",
                "action_name":"清空信息console",
            },
            {
                "x":1275,
                "y":197,
                "sleep":5,
                "name":"select_all_and_copy_and_paste",
                "content":"document.getElementsByClassName(\"cm-pagination-next\")[0].click()",
                "action_name":"切换产品",
            }
    ]
    for action_page_change in action_page_change_list:
        pyautogui_action(action_page_change)



