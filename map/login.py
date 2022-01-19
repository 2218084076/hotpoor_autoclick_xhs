from selenium import webdriver

import time

def getCookies():

    url = "http://www.dianping.com/"
    brower.get("https://account.dianping.com/login?redir=http%3A%2F%2Fwww.dianping.com%2F")
    while True:
        print("Please login in dianping.com!")
        time.sleep(3)

        while brower.current_url == url:
            tbCookies = brower.get_cookies()
            print(tbCookies)
            brower.quit()
# getCookies()
c_list = {'domain': '.dianping.com',
          'expiry': 1642239559,
          'httpOnly': False,
          'name': '_lxsdk_s',
          'path': '/',
          'secure': False,
          'value': '17e5cff8e3a-dd8-ccd-546%7C%7C6'}

brower=webdriver.Chrome()
brower.get('https://account.dianping.com/login?redir=https%3A%2F%2Fwww.dianping.com%2F')
brower.add_cookie({
    "domain": ".dianping.com",
    "name": c_list['name'],
    "value": c_list['value'],
    "path": '/',
})
brower.get('http://www.dianping.com/shop/128895900')
time.sleep(10)