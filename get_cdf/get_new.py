import pyautogui
import time
import pyperclip

# 打开审查元素位置 921.6
# 2022/01/15
urls=[" C021954","C037328"]

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
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press('enter')
    print(action.get("action_name"))
    action_sleep = action.get("sleep",0)
    time.sleep(action_sleep)

for u in urls:
    print(u)
    page={
        "x":800,
        "y":237,
        "sleep":5,
        "name":"url_paste",
        "content":u,
        "action_name":"访问链接",
    }
    pyautogui_action(page)
    action_item_click_list = [
        {
            "x": 198,
            "y": 951,
            "sleep": 0.5,
            "name": "move_to_click",
            "content": "",
            "action_name": "点击商品",
        },
        {
            "x": 454,
            "y": 20,
            "sleep": 0.5,
            "name": "open_console",
            "content": "",
            "action_name": "打开控制台",
        },
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
                '''
result=[]
result.push(document.getElementsByClassName("detail-box-title")[0].innerText)
result.push(document.getElementsByClassName("product-name")[0].innerText)
result.push(document.getElementsByClassName("product-code-value")[0].innerText)
result.push(document.getElementsByClassName("price-now")[0].innerText)

cxs=document.getElementsByClassName("promotion-item")
cxs_info = []
for (i=0;i<cxs.length;i++){
    cxs_info.push(cxs[i].innerText)
}
ths=document.getElementsByClassName("property-item-title")
tds=document.getElementsByClassName("property-item-value")
kv={}
for (i=0;i<ths.length;i++){
    kv[ths[i].innerText]=tds[i].innerText
}

result_info = {
    "detail-box-title":result[0],
    "product-name":result[1],
    "product-code-value":result[2],
    "price-now":result[3],
    "promotion-item":cxs_info,
    "property-item":kv,
}
                ''',
            "action_name": "get店铺信息",
        },
        {
            "x": 1376,
            "y": 997,
            "sleep": 0.5,
            "name": "select_all_and_copy_and_paste",
            "content":
                """
dom=document.createElement("div")
dom.id="wlb_cover"
dom.style.position="fixed"
dom.style.top="0px"
dom.style.right="0px"
dom.style.zIndex=9999999999999999999

                """,
            "action_name": "写入文本框textarea",
        },
        {
            "x": 1376,
            "y": 997,
            "sleep": 0.5,
            "name": "select_all_and_copy_and_paste",
            "content": rf'dom.innerHTML="<textarea id=\"wlb_cover_textarea\">"+JSON.stringify(result_info)+"</textarea>"',
            "action_name": "文本框展示",
        },
        {
            "x": 1376,
            "y": 997,
            "sleep": 0.5,
            "name": "select_all_and_copy_and_paste",
            "content": 'document.body.append(dom)',
            "action_name": "文本框展示",
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
            "x": 454,
            "y": 20,
            "sleep": 0.5,
            "name": "select_item_and_close_tab",
            "content": "",
            "action_name": "关闭选项卡",
        },
        {
            "x": 431,
            "y": 20,
            "sleep": 0.5,
            "name": "move_to_click",
            "content": "",
            "action_name": "点击选项卡_pages",
        },
        {
            "x": 468,
            "y": 219,
            "sleep": 0.5,
            "name": "select_all_and_paste",
            "content": "",
            "action_name": "提交",
        },
        {
            "x": 413,
            "y": 310,
            "sleep": 1,
            "name": "move_to_click",
            "content": "",
            "action_name": "submit",
        },
        {
            "x": 137,
            "y": 24,
            "sleep": 0.5,
            "name": "move_to_click",
            "content": "",
            "action_name": "切换pgy页面",
        },

    ]

    for action_item_click in action_item_click_list:

        pyautogui_action(action_item_click)



'''

result=[]
result.push(document.getElementsByClassName("shop-name")[0].innerText.split("\n")[0])
result.push(document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[0].getAttribute("class").split("mid-str")[1])
result.push(document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[1].innerText)
result.push(document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[2].innerText)
result.push(document.getElementsByClassName("tel")[0].innerText)
result.push(document.getElementsByClassName("address")[0].innerText)

result_info = {
    "shop-name":result[0],
    "star":result[1]*0.1,
    "comment":result[2],
    "consume":result[3],
    "tel":result[4],
    "address":result[5]
}

dom=document.createElement("div")
dom.id="wlb_cover"
dom.style.position="fixed"
dom.style.top="0px"
dom.style.right="0px"
dom.style.zIndex=9999999999999999999
dom.innerHTML="<textarea id=\"wlb_cover_textarea\">"+JSON.stringify(result_info)+"</textarea>"

document.body.append(dom)


shop-name = document.getElementsByClassName("shop-name")[0].innerText.split("\n")[0]
star = document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[0].getAttribute("class").split("mid-str")[1]
comment = document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[1].innerText
consume = document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[2].innerText
tel = document.getElementsByClassName("tel")[0].innerText
address = document.getElementsByClassName("address")[0].innerText


'''
