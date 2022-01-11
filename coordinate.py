import pyautogui
import time
while True:
    time.sleep(1)
    x,y = pyautogui.position()
    print('x=%s,y=%s'%(x,y))