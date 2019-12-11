# def bypass(driver, my_vars):
    # redirect = driver.find_element_by_xpath("/html/body/a")
    # print("redirect")

    # username = str(my_vars['uname'])
    # password = str(my_vars['passwd'])
    # siteBase = "blackboard.students.ptcollege.edu/auth-saml/saml/login?apId=_202_1&redirectUrl=https%3A%2F%2Fblackboard.students.ptcollege.edu%2Fwebapps%2Fportal%2Fexecute%2FdefaultTab"
    # schoolDomain = str(my_vars['schoolDomain'])
    #
    # URL = "http://" + username + ":" + password + "@" + siteBase
    # driver.get(URL)
    # # usernameEle = driver.find_element_by_id("userNameInput")
    # # usernameEle.send_keys(schoolDomain + username)
    # # passwordEle = driver.find_element_by_id("passwordInput")
    # # passwordEle.send_keys(password)
    # # passwordEle.submit()
    # print(driver.page_source)

from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import os

bravePath = os.getenv('localappdata') + "\BraveSoftware\Brave-Browser\Application"
options = Options()
options.binary_location = bravePath + "/brave.exe"
chromeDriver = ChromeDriverManager().install()
browser = webdriver.Chrome(options=options, executable_path=chromeDriver)
print("driver started")


siteBase = "blackboard.students.ptcollege.edu/"
#URL = "https://" + "jjf27" + ":" + "J3st3r1998" + "@" + siteBase
URL = "https://" + siteBase
print(URL + " " + "URL")
browser.get(URL)
try:
    # redirect = browser.find_element_by_xpath("/html/body/a")
    #browser.get(redirect.get_attribute("href"))
    # element = WebDriverWait(browser, 10).until(EC.url_changes("https://adfs.ptcollege.edu/"))
    if(EC.url_changes()):
        print(browser.current_url)
    else:
        time.sleep(1)

finally:
    time.sleep(20)
    driver.quit()


# print(browser.title)
# # link = browser.find_element_by_xpath("/html/body/a")
# print("bleb")
# print(str(browser.current_url))
# time.sleep(4)
# newURL = browser.current_url
# print(browser.title)
# newURL = ("https://" + "jjf27" + ":" + "J3st3r1998" + "@" + newURL.replace("https://",""))
# browser.get(newURL)
#
# # URLTwo = "https://"+"jjf27" + ":" + "J3st3r1998" + "@" + siteBase
# browser.get(URLTwo)
# time.sleep(5)
# print(browser.current_url)
# browser.get(URLTwo)