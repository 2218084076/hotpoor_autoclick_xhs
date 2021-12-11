import os
import time
import pyautogui

n=1
while True:


    time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 283 500")
    time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 1012 155")
    time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 324 1997")
    pyautogui.click(1538,336)
    time.sleep(2)
    pyautogui.hotkey('ctrl','a')
    time.sleep(2)
    pyautogui.hotkey('ctrl','v')
    time.sleep(2)
    pyautogui.click(1400,397)
    time.sleep(25)
    # pyautogui.click(1536,251)
    # time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 71 120")
    time.sleep(2)


    os.system("adb -s 869e65410721 shell input tap 263 1457")
    time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 1012 155")
    time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 324 1997")
    pyautogui.click(1538,336)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(2)
    pyautogui.hotkey('ctrl','v')
    time.sleep(2)
    pyautogui.click(1400,397)
    time.sleep(25)
    # pyautogui.click(1536, 251)
    # time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 71 120")
    time.sleep(2)
    os.system("adb -s 869e65410721 shell input swipe 528 1926 528 262 500")
    print(n)
    n+=1