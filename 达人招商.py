import pyautogui
from time import sleep
import pyperclip
import os
while True:
    for n in range(0,20):
        pyautogui.moveTo(x=1583,y=179, duration=0.3)
        pyautogui.click(x=1583,y=179, button='left')
        pyautogui.moveTo(x=1583,y=179, duration=0.3)
        pyautogui.click(x=1583,y=179, button='left')
        sleep(1)
        pyautogui.moveTo(x=1611,y=917, duration=0.3)
        pyautogui.click(x=1611,y=917, button='left')
        sleep(1)
        pyautogui.typewrite(f'document.getElementsByClassName("business-activity-container")[{n}].getElementsByTagName("button")[0].click()')
        pyautogui.keyDown('enter')
        sleep(2)

        pyautogui.typewrite('document.getElementsByClassName("ant-table-cell ant-table-cell-fix-right ant-table-cell-fix-right-first")[1].getElementsByTagName("div")[0].click()')
        pyautogui.keyDown('enter')
        sleep(1)

        pyautogui.moveTo(x=995,y=292,duration=0.3)
        pyautogui.click(x=995,y=292, button='left')
        pyautogui.typewrite("138")
        sleep(0.5)
        pyautogui.moveTo(x=996,y=349,duration=0.3)
        pyautogui.click(x=996,y=349, button='left')
        pyautogui.typewrite("30")
        sleep(0.5)
        pyautogui.moveTo(x=1165,y=354,duration=0.3)
        pyautogui.click(x=1165,y=354, button='left')
        sleep(0.5)
        pyautogui.moveTo(x=999, y=435,duration=0.3)
        pyautogui.click(x=999, y=435, button='left')
        pyautogui.typewrite("1000000")
        sleep(0.5)
        pyautogui.moveTo(x=1031,y=767,duration=0.3)
        pyautogui.click(x=1031,y=767, button='left')
        pyperclip.copy("我们是Puco唇泥,产品质量好,在寻求合作伙伴~佣金可以谈 生产的工厂是科丝美诗,前期已经在小红书上面有一定的声量,淘系顶流店铺都已铺货,销售量客观,期待和你合作")
        pyautogui.hotkey('ctrl','v')
        sleep(1)

        pyautogui.moveTo(x=1300,y=977, duration=0.3)
        pyautogui.click(x=1300,y=977, button='left')
        sleep(2)
        pyautogui.moveTo(x=22,y=62,duration=0.3)
        pyautogui.click(x=22,y=62,button='left')
        sleep(6)

        pyautogui.moveTo(x=111, y=420,duration=0.3)
        pyautogui.click(x=111, y=420, button='left')

        pyautogui.moveTo(x=1168, y=333, duration=0.3)
        pyautogui.click(x=1168, y=333, button='left')
        sleep(3)

    pyautogui.moveTo(x=1168, y=333, duration=0.3)
    pyautogui.click(x=1168, y=333, button='left')

    pyautogui.moveTo(x=1583,y=179, duration=0.3)
    pyautogui.click(x=1583,y=179, button='left')
    pyautogui.moveTo(x=1583,y=179, duration=0.3)
    pyautogui.click(x=1583,y=179, button='left')
    sleep(1)
    pyautogui.moveTo(x=1611,y=917, duration=0.3)
    pyautogui.click(x=1611,y=917, button='left')

    pyautogui.typewrite('scrollBy(100,9999)')
    pyautogui.keyDown('enter')
    sleep(2)


# Js window.location.href  获取网页url
