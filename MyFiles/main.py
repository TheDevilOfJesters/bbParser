import time
from selenium import webdriver
from login.blackboardlogin import login
from dostuff.navigateToAssignments import getClassNames
from setup.jsonread import json_read
from setup.localSetup import setup_local_folder
from setup.seleniumsetup import setup, teardown


driver = webdriver
my_vars = json_read()
setup_local_folder(my_vars)
driver = setup(my_vars)
login(driver, my_vars)
# bypass(DRIVER, MYVAR)
getClassNames(driver, my_vars)

time.sleep(5)

teardown(driver)
