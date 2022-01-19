from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import xlwt
import random

brower=webdriver.Chrome()

brower.get('http://www.cdfgsanya.com/brand-shop.html?id=248309&name=SK-II&nameEN=SK-II&isShowBrandInfo=false')
time.sleep(8)
