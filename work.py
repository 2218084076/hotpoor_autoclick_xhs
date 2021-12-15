import uiautomator2 as u2
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import os


d = u2.connect_usb('aeebf218')
def click_text(self,str,sq=0):
    path=d(text=str)[sq]
    x,y=path.center()
    d.click(x,y)
def click(card_ty):
    d.app_start("com.tencent.wework")
    time.sleep(5)
    d(text="工作台").click()
    time.sleep(3)
    d(text="打卡").click()
    time.sleep(3)
    d(text="").click()
    time.sleep(3)
    d(scrollable=True).fling.toEnd()
    click_text(d,card_ty,-1)
    time.sleep(3)
    d.app_stop("com.tencent.wework")
def job1():
    click("上班打卡")
def job2():
    click("下班打卡")
if __name__ == "__main__":
    sched = BlockingScheduler()
    sched.add_job(job1,'cron',day_of_week='mon-fri',hour='10',minute='00')
    sched.add_job(job2,'cron',day_of_week='mon-fri',hour='19',minute='12')
    sched.start()