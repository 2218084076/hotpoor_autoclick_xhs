import pyautogui

def move_and_click(x,y,sleeptime):
    pyautogui.moveTo(x=x, y=y,duration=0, tween=pyautogui.linear)
    pyautogui.click(x=x, y=y,clicks=1, button='left')
    pyautogui.sleep(sleeptime)
def move_and_click_input_enter(x,y,sleeptime,input_str,press,select_all=False):
    pyautogui.moveTo(x=x, y=y,duration=0, tween=pyautogui.linear)
    pyautogui.click(x=x, y=y,clicks=1, button='left')
    if select_all:
        pyautogui.hotkey("ctrl", "a")
    pyautogui.typewrite(input_str)
    pyautogui.press(press)
    pyautogui.sleep(sleeptime)
def move_and_click_select_copy(x,y,sleeptime):
    pyautogui.moveTo(x=x, y=y,duration=0, tween=pyautogui.linear)
    pyautogui.click(x=x, y=y,clicks=1, button='left')
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    pyautogui.sleep(sleeptime)
def move_and_click_paste(x,y,sleeptime):
    pyautogui.moveTo(x=x, y=y,duration=0, tween=pyautogui.linear)
    pyautogui.click(x=x, y=y,clicks=1, button='left')
    pyautogui.hotkey("ctrl", "v")
    pyautogui.sleep(sleeptime)
def click_enter(x,y):
    pyautogui.moveTo(x=x, y=y,duration=0, tween=pyautogui.linear)
    pyautogui.click(x=x, y=y,clicks=1, button='left')
    pyautogui.press('enter')
def start_page(num):
    #点击console
    move_and_click(1100,141,2)
    #清除console里面的内容
    move_and_click(968,177,2)
    move_and_click_input_enter(1005,248,1,'$("input.corona_input[data-v-5f5cbc17]").value=%s'%num,'enter')
    click_enter(808,701)
    pyautogui.sleep(3)
num=295
end_num = 364
#网页地点730.4 and 704.8
#刷新第一页
#清除blogger/v2
move_and_click(1153,250,2)
#清除response
move_and_click(1230,216,2)
start_page(num)
for i in range(num,end_num):
    print("执行第%s页"%(i))
    #跳转到network
    move_and_click(1314,183,1)
    #移动到fetch
    move_and_click(1252,280,1)
    #enter blogger/v2
    move_and_click_input_enter(1053,250,3,"/api/solar/cooperator/blogger/v2",'enter',True)
    #点击 blogger/v2
    move_and_click(1060,321,1)
    #点击response
    move_and_click(1461,443,1)
    #移动到data,并点击，复制
    move_and_click_select_copy(1430,473,1)
    #移除response
    move_and_click(1230,217,1)
    #点击粘贴界面
    move_and_click(420,22,1)
    #刷新粘贴界面
    move_and_click(107,65,2)
    #找到粘贴地方，并粘贴
    move_and_click_paste(450,220,1)
    #点击提交
    move_and_click(455,323,2)
    #点击回原小红书
    move_and_click(126,21,1)
    #点击console
    move_and_click(1150,184,2)
    #清除console里面的内容
    move_and_click(990,217,2)
    #点击console,并跳转下一页
    move_and_click_input_enter(1005,248,1,'$(".corona-pagination_pagination").children[$(".corona-pagination_pagination").children.length-1].click()','enter')
    #清除console里面的内容
    move_and_click(990,217,2)