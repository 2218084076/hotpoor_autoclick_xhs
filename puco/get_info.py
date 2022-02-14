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
    elif action["name"] in ["select_item_and_close_tab"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "w")
    print(action.get("action_name"))
    action_sleep = action.get("sleep",0)
    time.sleep(action_sleep)
# while True:
for u in range(0,1):
    for i in range(0,11):
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
                "sleep": 5,
                "name": "select_all_and_copy_and_paste",
                "content":'document.getElementsByClassName("daren-card")[%s].click()'%(i),
                "action_name": "点击博主页面",
            },
            {
                "x": 427,
                "y": 21,
                "sleep": 0.5,
                "name": "open_console",
                "content": '',
                "action_name": "打开console"
            },
            {
                "x": 193,
                "y": 261,
                "sleep": 0.5,
                "name": "move_to_click",
                "content": "",
                "action_name": "点击抖音号",
            },
            {
                "x": 193,
                "y": 261,
                "sleep": 0.5,
                "name": "move_to_click",
                "content": "",
                "action_name": "点击抖音号",
            },
            {
                "x": 1204,
                "y": 172,
                "sleep": 0.5,
                "name": "move_to_click",
                "content": "",
                "action_name": "清空信息console",
            },
            {
                "x": 1282,
                "y": 995,
                "sleep": 1,
                "name": "select_all_and_copy_and_paste",
                "content":     '''  
result=[]
result.push(document.getElementsByClassName("daren-overview-base-nameblock")[0].innerText)
result.push(document.getElementsByClassName("daren-overview-base-basepoints__block-value")[2].innerText)
result.push(document.getElementsByClassName("data-overview-dashboard-items-item__value")[3].innerText)
try{
result.push(document.getElementsByClassName("contact_way_info_block_item")[0].innerText)
}catch{
    result.push("no wechat")}
try{
result.push(document.getElementsByClassName("contact_way_info_block_item")[1].innerText)
}catch{
    result.push("no phone")}
result.push(document.getElementsByClassName("daren-overview-base-info__content-item")[2].innerText)
result.push(document.getElementsByClassName("qrcode-content-info-account")[0].innerText)
result_info={
    "name":result[0],
    "fan":result[1],
    "shop":result[2],
    "wechat":result[3],
    "phone":result[4],
    "introduce":result[5],
    "dou_id":result[6],
}
console.log(result_info)
dom=document.createElement("div")
dom.id="wlb_cover"
dom.style.position="fixed"
dom.style.top="0px"
dom.style.right="0px"
dom.style.zIndex=9999999999999999999
    ''',
                "action_name": "获取信息",
            },
            {
                "x": 1282,
                "y": 995,
                "sleep": 1,
                "name": "select_all_and_copy_and_paste",
                "content": rf'dom.innerHTML="<textarea id=\"wlb_cover_textarea\">"+JSON.stringify(result_info)+"</textarea>"',
                "action_name": "展示textarea文本框"
            },
            {
                "x": 1282,
                "y": 995,
                "sleep": 1,
                "name": "select_all_and_copy_and_paste",
                "content": 'document.body.append(dom)',
                "action_name": "展示textarea文本框"
            },
            {
                "x": 1023,
                "y": 152,
                "sleep": 1,
                "name": "select_all_and_copy",
                "content": "",
                "action_name": "copy"
            },
            {
                "x": 430,
                "y": 14,
                "sleep": 1,
                "name": "select_item_and_close_tab",
                "content": "",
                "action_name": "select_item_and_close_tab"
            },
            {
                "x": 459,
                "y": 19,
                "sleep": 0.5,
                "name": "move_to_click",
                "content": "",
                "action_name": "切换console",
            },
            {
                "x": 540,
                "y": 248,
                "sleep": 1,
                "name": "select_all_and_paste",
                "content": '',
                "action_name": "粘贴"
            },
            {
                "x": 412,
                "y": 311,
                "sleep": 0.5,
                "name": "move_to_click",
                "content": "",
                "action_name": "submit",
            },
            {
                "x": 97,
                "y": 21,
                "sleep": 0.5,
                "name": "move_to_click",
                "content": "",
                "action_name": "切换console",
            },
            {
                "x": 1204,
                "y": 172,
                "sleep": 0.5,
                "name": "move_to_click",
                "content": "",
                "action_name": "清空信息console",
            },
        ]
        for action_item_click in action_item_click_list:
            pyautogui_action(action_item_click)
    next=[{
        "x": 1282,
        "y": 995,
        "sleep": 1,
        "name": "select_all_and_copy_and_paste",
        "content": 'document.getElementsByClassName("ant-pagination-item-link")[3].click()',
        "action_name": "下一页"
    }]
    for click in next:
        pyautogui_action(click)

'''
result=[]
result.push(document.getElementsByClassName("daren-overview-base-nameblock")[0].innerText)
result.push(document.getElementsByClassName("daren-overview-base-basepoints__block-value")[2].innerText)
result.push(document.getElementsByClassName("data-overview-dashboard-items-item__value")[3].innerText)
try{
result.push(document.getElementsByClassName("contact_way_info_block_item")[0].innerText.split("微信号")[1])
}catch{
    result.push(" ")}
try{
result.push(document.getElementsByClassName("contact_way_info_block_item")[0].innerText.split("微信号")[1])
}catch{
    result.push(" ")}
result.push(document.getElementsByClassName("daren-overview-base-info__content-item")[2].innerText)
result.push(document.getElementsByClassName("qrcode-content-info-account")[0].innerText)
result_info={
    "name":result[0],
    "fan":result[1],
    "shop":result[2],
    "wechat":result[3],
    "phone":result[4],
    "introduce":result[5],
    "dou_id":result[6],
}
console.log(result_info)
dom=document.createElement("div")
dom.id="wlb_cover"
dom.style.position="fixed"
dom.style.top="0px"
dom.style.right="0px"
dom.style.zIndex=9999999999999999999
dom.innerHTML="<textarea id=\"wlb_cover_textarea\">"+JSON.stringify(result_info)+"</textarea>"
document.body.append(dom)
'''