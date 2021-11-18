import os
import time

b = 0

def video():
    fun = os.system('adb shell input swipe 300 600 300 100')  ##坐标根据需要自己修改滑动
    time.sleep(3)
def zan():
    #fun1 =os.system(" adb shell input tap 89 79")  ##坐标根据需要自己修改  直播坐标
    #fun1 = os.system(" adb shell input tap 85 1000")  ##坐标根据需要自己修改    音乐坐标
    #fun1 = os.system(" adb shell input tap 85 900")  ##坐标根据需要自己修改    进主页坐标
    fun1 = os.system(" adb shell input tap 620 600")  ##坐标根据需要自己修改    点赞坐标
    time.sleep(3)

def pinglun():
    #fun1 =os.system(" adb shell input tap 89 79")  ##坐标根据需要自己修改  直播坐标
    #fun1 = os.system(" adb shell input tap 85 1000")  ##坐标根据需要自己修改    音乐坐标
    #fun1 = os.system(" adb shell input tap 85 900")  ##坐标根据需要自己修改    进主页坐标
    fun1 = os.system(" adb shell input tap 620 750")  ##坐标根据需要自己修改    评论坐标
    fun1 = os.system(" adb shell input tap 620 750")  ##坐标根据需要自己修改    评论坐标
    time.sleep(3)


def fanhui():
    fun12 =os.system(" adb shell input tap 85 70")  ##坐标根据需要自己修改  直播he 返回 坐标
    time.sleep(6)
if __name__ == '__main__':
    os.chdir("D:/adb")  ##切换到adb所在目录可以自己修改
    print("已连接设备名称如下:")
    os.system('adb version')
    fun = os.system('adb devices')

    a = 100
    a = int(a)
    while b < a:
        #zan()
        #fanhui()
        pinglun()
        video()  ##循环结构中调用函数

        b = b + 1
        print("任务完成", b, "次")
else:
    print("任务全部完成")
    fun = os.system('adb kill-server')  ##运行结束杀掉adb进程
    exit()
