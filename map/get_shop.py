import pyautogui
import time
import pyperclip

# 打开审查元素位置 921.6
# 2022/01/15
news_urls=[]
for i in urls:
    news_urls.append(i)
print(len(urls))
print(len(news_urls))
print(len(news_urls))
print(len(news_urls))

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
    elif action["name"] in ["url_paste"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        write_content = action.get("content","")
        pyperclip.copy(write_content)
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "l")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press('enter')
    print(action.get("action_name"))
    action_sleep = action.get("sleep",0)
    time.sleep(action_sleep)

for u in urls:
    print(u)
    page={
        "x":435,
        "y":69,
        "sleep":8,
        "name":"select_all_and_copy_and_paste",
        "content":'document.getElementsByClassName("pic")[0].getElementsByTagName("a")[0].click()',
        "action_name":"访问链接",
    }
    pyautogui_action(page)
    action_item_click_list = [
        {
            "x": 1207,
            "y": 176,
            "sleep": 0.5,
            "name": "move_to_click",
            "content": "",
            "action_name": "清空console",
        },
        {
            "x": 1376,
            "y": 997,
            "sleep": 0.5,
            "name": "select_all_and_copy_and_paste",
            "content":
                r'''
result=[]
result.push(document.getElementsByClassName("shop-name")[0].innerText)
result.push(document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[0].getAttribute("class").split("mid-str")[1])
result.push(document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[1].innerText)
try{
result.push(document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[2].innerText)
}catch{
result.push("null")
}
try{
result.push(document.getElementsByClassName("tel")[0].innerText)
}catch{
document.getElementsByClassName("phone")[0].getElementsByTagName("a")[0].click()
result.push(document.getElementsByClassName("phone")[0].innerText)
}
result.push(document.getElementsByClassName("address")[0].innerText)
result.push(document.getElementById("map").getElementsByTagName("img")[0].getAttribute("src").split(".png|")[1])
result_info = {
"shop-name":result[0],
"star":result[1]*0.1,
"comment":result[2],
"consume":result[3],
"tel":result[4],
"address":result[5],
"coordinate":result[6],
}
dom=document.createElement("div")
dom.id="wlb_cover"
dom.style.position="fixed"
dom.style.top="0px"
dom.style.right="0px"
dom.style.zIndex=9999999999999999999
dom.innerHTML="<textarea id=\"wlb_cover_textarea\" style=\"height:100px;width:200px;\">"+JSON.stringify(result_info)+"</textarea>"
document.body.append(dom)
                ''',
            "action_name": "get店铺信息",
        },
        {
            "x": 1026,
            "y": 149,
            "sleep": 0.5,
            "name": "select_all_and_copy",
            "content": "",
            "action_name": "copy"
        },
        {
            "x": 431,
            "y": 20,
            "sleep": 1,
            "name": "move_to_click",
            "content": "",
            "action_name": "点击选项卡_pages",
        },
        {
            "x": 533,
            "y": 209,
            "sleep": 1,
            "name": "select_all_and_paste",
            "content": "",
            "action_name": "提交",
        },
        {
            "x": 416,
            "y": 283,
            "sleep": 1,
            "name": "move_to_click",
            "content": "",
            "action_name": "submit",
        },
        {
            "x": 137,
            "y": 24,
            "sleep": 1,
            "name": "move_to_click",
            "content": "",
            "action_name": "切换pgy页面",
        },

    ]
    for action_item_click in action_item_click_list:
        pyautogui_action(action_item_click)



'''
result=[]
result.push(document.getElementsByClassName("shop-name")[0].innerText)
result.push(document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[0].getAttribute("class").split("mid-str")[1])
result.push(document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[1].innerText)
try{
result.push(document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[2].innerText)
}catch{
result.push("null")
}
try{
result.push(document.getElementsByClassName("tel")[0].innerText)
}catch{
document.getElementsByClassName("phone")[0].getElementsByTagName("a")[0].click()
result.push(document.getElementsByClassName("phone")[0].innerText)
}
result.push(document.getElementsByClassName("address")[0].innerText)
result.push(document.getElementById("map").getElementsByTagName("img")[0].getAttribute("src").split(".png|")[1])
result_info = {
"shop-name":result[0],
"star":result[1]*0.1,
"comment":result[2],
"consume":result[3],
"tel":result[4],
"address":result[5],
"coordinate":result[6],
}
dom=document.createElement("div")
dom.id="wlb_cover"
dom.style.position="fixed"
dom.style.top="0px"
dom.style.right="0px"
dom.style.zIndex=9999999999999999999
dom.innerHTML="<textarea id=\"wlb_cover_textarea\" style=\"height:100px;width:200px;\">"+JSON.stringify(result_info)+"</textarea>"
document.body.append(dom)
'''
