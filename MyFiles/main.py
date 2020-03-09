import time
from selenium import webdriver
from login.blackboardlogin import login
from dostuff.navigateToAssignments import getClassNames
from setup.jsonread import json_read
from setup.localSetup import setupLocalFolder
from setup.seleniumsetup import setup, teardown


DRIVER = webdriver
myvars = json_read()
setupLocalFolder(myvars)
DRIVER = setup(DRIVER, myvars)
login(DRIVER, myvars)
# bypass(DRIVER, MYVAR)
getClassNames(DRIVER, myvars)

time.sleep(5)

teardown(DRIVER)