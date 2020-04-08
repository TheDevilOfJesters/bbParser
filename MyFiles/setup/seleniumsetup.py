# import
import os
from os import path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager


def setup(my_vars):
    options = Options()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-default-apps")
    options.add_argument("--start-maximized")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--headless")
    driver = getBrowser(options, my_vars)
    return driver


def teardown(driver):
    driver.close()


def getBrowser(options, my_vars):
    browser = str(my_vars['browser'])

    brave_path = os.getenv("programfiles(x86)") + "\BraveSoftware\Brave-Browser\Application"
    chrome_path = os.getenv("programfiles(x86)") + "\Google\Chrome\Application"
    firefox_path = os.getenv("programfiles") + "\Mozilla Firefox"
    opera_path = os.getenv("localappdata") + "\Programs\Opera"
    # IEPath = os.getenv("programfiles")

    if path.isdir(brave_path) and browser.lower() == "brave":
        options.binary_location = brave_path + "\\brave.exe"
        chrome_driver = getChromeDriver()
        driver = webdriver.Chrome(options=options, executable_path=chrome_driver)
        return driver
    elif path.isdir(firefox_path) and browser.lower() == "firefox":
        options.binary_location = firefox_path + "/firefox.exe"
        firefox_driver = getFirefoxDriver()
        driver = webdriver.Firefox(executable_path=firefox_driver)
        return driver
    elif path.isdir(chrome_path) and browser.lower() == "chrome":
        options.binary_location = chrome_path + "/chrome.exe"
        chrome_driver = getChromeDriver()
        driver = webdriver.Chrome(options=options, executable_path=chrome_driver)
        return driver
    elif path.isdir(opera_path) and browser.lower() == "opera":
        options = webdriver.ChromeOptions()
        options.add_argument('allow-elevated-browser')
        version = str(max([os.path.join(opera_path, d) for d in os.listdir(opera_path)], key=os.path.getmtime))
        options.binary_location = version + "/opera.exe"
        opera_driver = getOperaDriver()
        driver = webdriver.Opera(options=options, executable_path=opera_driver)
        return driver
    else:
        options.binary_location = chrome_path + "/chrome.exe"
        chrome_driver = getChromeDriver()
        driver = webdriver.Chrome(options=options, executable_path=chrome_driver)
        return driver

    # driver = webdriver.Ie(IEDriverManager().install())


def getChromeDriver():
    chrome_driver = ChromeDriverManager().install()
    return chrome_driver


def getFirefoxDriver():
    firefox_driver = GeckoDriverManager().install()
    return firefox_driver


def getOperaDriver():
    opera_driver = OperaDriverManager().install()
    return opera_driver
