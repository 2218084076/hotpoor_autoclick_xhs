#-*-coding: utf-8 -*-

import os
import time
import random
import json
import shutil

json_files = os.listdir(r'D:\github\1\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\files')
pic_files = os.listdir(r'D:\github\1\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\upload')
plane_file1 = r'D:\github\1\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\upload\plane\619e24ad000000002103e233_0.jpg'
plane_file2 = r"D:\github\1\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\upload\plane\619e24ad000000002103e233_1.jpg"
s_files = os.listdir(r'D:\github\1\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\s')

def set_file_time(filename, updatetime, access_time):
    # 先传修改时间，再传访问时间
    filename = os.path.abspath(filename)
    new_updatetime = time.mktime(time.strptime(updatetime, '%Y-%m-%d %H:%M:%S'))
    new_access_time = time.mktime(time.strptime(access_time, '%Y-%m-%d %H:%M:%S'))
    os.utime(filename, (new_access_time, new_updatetime))

# puco返航计划



num = 1
os.system('adb -s 869e65410721 shell ime set com.android.adbkeyboard/.AdbIME')
for id in json_files:
    if id in s_files:
        print('skip')
    else:
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        pic = []
        for p in pic_files:
            if id.split('.json')[0] == p.split('_')[0]:
                pic.append(p)
        for n in pic[-4:-1]:
            print(n)
            if __name__ == '__main__':
                set_file_time(f'D:/github/1/hotpoor_autoclick_xhs/mac_xialiwei_256/local_web/static/upload/{n}', now_time, now_time)
            os.system(f'adb -s 869e65410721 push D:/github/1/hotpoor_autoclick_xhs/mac_xialiwei_256/local_web/static/upload/{n} /sdcard/DCIM/Camera')
        os.system('adb -s 869e65410721 shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera/')
        time.sleep(0.5)
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if __name__ == '__main__':
            set_file_time(f'{plane_file1}', now_time, now_time)
            set_file_time(f'{plane_file2}', now_time, now_time)
        os.system(f'adb -s 869e65410721 push {plane_file2} /sdcard/DCIM/Camera')
        os.system(f'adb -s 869e65410721 push {plane_file1} /sdcard/DCIM/Camera')

        os.system('adb -s 869e65410721 shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera/')
        print('打开小红书\n')
        os.system('adb -s 869e65410721 shell ime set com.android.adbkeyboard/.AdbIME')
        os.system("adb -s 869e65410721 shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1")
        time.sleep(8)

        print('点击小红书发布加号\n')
        os.system("adb -s 869e65410721 shell input tap 540 2151")
        time.sleep(5)

        print("选择图片\n")

        os.system('adb -s 869e65410721 shell input tap 311 758')
        os.system('adb -s 869e65410721 shell input tap 675 411')
        os.system('adb -s 869e65410721 shell input tap 306 411')
        os.system('adb -s 869e65410721 shell input tap 1037 411')
        os.system('adb -s 869e65410721 shell input tap 670 774')
        print('下一步\n')
        os.system("adb -s 869e65410721 shell input tap 931 2144")
        time.sleep(2)
        print('下一步\n')
        os.system("adb -s 869e65410721 shell input tap 998 162")
        time.sleep(3)
        print('等待文案\n')

        js_path = rf'D:\github\1\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\files\{id}'
        print(js_path)
        data =json.load(open(js_path,encoding='utf-8'))
        title = data['title']


        title.split('\n')
        content = data['content']
        content = content.replace('@', '!')
        title = title.replace('PUCO', '唇泥')
        content = content.split('\n')
        user_name = data['user_name']

        print(content)
        os.system("adb -s 869e65410721 shell input tap 240 623")
        time.sleep(0.5)
        print("粘贴文案")
        for t in title:
            os.system(f'adb -s 869e65410721 shell am broadcast -a ADB_INPUT_TEXT --es msg  "{t}"')
            # os.system('adb -s 869e65410721 shell input keyevent KEYCODE_ENTER')
        time.sleep(2)
        os.system("adb -s 869e65410721 shell input tap 491 820")
        time.sleep(2)
        for c in content:
            os.system(f'adb -s 869e65410721 shell am broadcast -a ADB_INPUT_TEXT --es msg "{c}"')
            os.system('adb -s 869e65410721 shell input keyevent KEYCODE_ENTER')
        time.sleep(2)

        os.system('adb -s 869e65410721 shell ime set com.iflytek.inputmethod.miui/.FlyIME')
        time.sleep(2)
        # os.system('adb -s 869e65410721 shell ime set com.android.adbkeyboard/.AdbIME')
        time.sleep(1)
        os.system("adb -s 869e65410721 shell input tap 118 527")
        time.sleep(1)
        os.system('adb -s 869e65410721 shell input text "p"')
        os.system('adb -s 869e65410721 shell input text "u"')
        os.system('adb -s 869e65410721 shell input text "c"')
        os.system('adb -s 869e65410721 shell input text "o"')
        os.system('adb -s 869e65410721 shell ime set com.android.adbkeyboard/.AdbIME')
        time.sleep(1)
        os.system(f'adb -s 869e65410721 shell am broadcast -a ADB_INPUT_TEXT --es msg  "返航计划"')
        time.sleep(2)
        os.system('adb -s 869e65410721 shell ime set com.iflytek.inputmethod.miui/.FlyIME')
        time.sleep(1)
        os.system("adb -s 869e65410721 shell input tap 329 518")
        time.sleep(1)
        os.system('adb -s 869e65410721 shell ime set com.android.adbkeyboard/.AdbIME')
        time.sleep(2)
        os.system(f'adb -s 869e65410721 shell am broadcast -a ADB_INPUT_TEXT --es msg  "{user_name}"')
        time.sleep(2)
        os.system("adb -s 869e65410721 shell input tap 185 1215")
        time.sleep(2)
        os.system("adb -s 869e65410721 shell input tap 649 2100")
        time.sleep(2)
        print(user_name)
        print(id)
        print(id)
        print(id)
        print(id)
        print('发布\n')
        time.sleep(15)
        os.system("adb -s 869e65410721 shell input tap 766 2272")
        time.sleep(2)
        os.system("adb -s 869e65410721 shell input tap 978 2137")
        time.sleep(2)
        os.system("adb -s 869e65410721 shell input tap 978 2137")
        time.sleep(2)
        os.system("adb -s 869e65410721 shell input tap 978 2137")
        time.sleep(2)
        os.system(f"adb -s 869e65410721 shell input swipe 533 271 647 1608 150")

        time.sleep(60 * 2)
        print('start\n')
        print(id)
        i = 1
        while i < 6:
            x1 = random.randint(86, 482)
            y1 = random.randint(1172, 1629)
            a = random.randint(2, 5)
            os.system(f"adb -s 869e65410721 shell input tap {x1} {y1}")
            os.system(f"adb -s 869e65410721 shell input swipe 951 994 80 975 100")
            os.system(f"adb -s 869e65410721 shell input swipe 951 994 80 975 100")
            os.system(f"adb -s 869e65410721 shell input swipe 951 994 80 975 100")
            time.sleep(a)
            os.system(f"adb -s 869e65410721 shell input tap 766 2261")
            time.sleep(2)
            print(f'n={i} t={a} (x{x1},y{y1})')
            i += 1
        print(f"{id}\tEnd")
        os.system("adb -s 869e65410721 shell input tap 766 2261")
        time.sleep(0.5)
        os.system("adb -s 869e65410721 shell input tap 766 2261")
        time.sleep(0.5)
        os.system("adb -s 869e65410721 shell input tap 766 2261")
        time.sleep(0.5)
        os.system("adb -s 869e65410721 shell input tap 766 2261")
        shutil.copy(f'{js_path}','D:/github/1/hotpoor_autoclick_xhs/mac_xialiwei_256/local_web/static/s')
        os.remove(js_path)
        print(f"num{num}")
        num+=1

        

#  security find-generic-password -ga "ROUTERNAME" | grep "password:"