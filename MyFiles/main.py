from setup.seleniumsetup import setup, teardown
# from blackboardTesting import setup, teardown
from login.blackboardlogin import login
from setup.jsonread import json_read
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os.path
from os import path
import sys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from login.bypass import bypass



# dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)

DRIVER = webdriver

FILE = "variables.json"
MYVAR = json_read(FILE)
DRIVER = setup(DRIVER, MYVAR)
#login(DRIVER, MYVAR)
bypass(DRIVER, MYVAR)

time.sleep(5)

teardown(DRIVER)
