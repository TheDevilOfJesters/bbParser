from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os.path
from os import path
import sys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager

def setup(driver, my_vars):
    options = Options()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-default-apps")
    options.add_argument("--start-maximized")
        # options.add_argument("--disable-gpu")
        # options.add_argument("--headless")
        # driver = webdriver.Chrome(chrome_options=options, executable_path=chromedriver_path)
    driver = getBrowser(options, my_vars)
    return driver

def teardown(driver):
    driver.close()

def getBrowser(options, myvars):

    browser = str(myvars['browser'])

    bravePath = os.getenv('localappdata') + "\BraveSoftware\Brave-Browser\Application"
    chromePath = os.getenv("programfiles(x86)") + "\Google\Chrome\Application"
    firefoxPath = os.getenv("programfiles") + "\Mozilla Firefox"
    operaPath = os.getenv("localappdata") + "\Programs\Opera"
    # IEPath = os.getenv("programfiles")

    if (path.isdir(bravePath) and browser.lower() == "brave"):
        options.binary_location = bravePath + "\\brave.exe"
        chromeDriver = getChromeDriver()
        driver = webdriver.Chrome(options=options, executable_path=chromeDriver)
        return(driver)
    elif (path.isdir(firefoxPath) and browser.lower() == "firefox"):
        options.binary_location = firefoxPath + "/firefox.exe"
        firefoxDriver =getFirefoxDriver()
        driver = webdriver.Firefox(executable_path=firefoxDriver)
        return(driver)
    elif (path.isdir(chromePath) and browser.lower() == "chrome"):
        options.binary_location = chromePath + "/chrome.exe"
        chromeDriver = getChromeDriver()
        driver = webdriver.Chrome(options=options, executable_path=chromeDriver)
        return(driver)
    elif (path.isdir(operaPath) and browser.lower() == "opera"):
        options = webdriver.ChromeOptions()
        options.add_argument('allow-elevated-browser')
        version = str(max([os.path.join(operaPath, d) for d in os.listdir(operaPath)], key=os.path.getmtime))
        options.binary_location = version + "/opera.exe"
        operaDriver =getOperaDriver()
        driver = webdriver.Opera(options=options, executable_path=operaDriver)
        return(driver)
    else:
        options.binary_location = chromePath + "/chrome.exe"
        chromeDriver = getChromeDriver()
        driver = webdriver.Chrome(options=options, executable_path=chromeDriver)
        return(driver)

    # driver = webdriver.Ie(IEDriverManager().install())

def getChromeDriver():
    chromeDriver = ChromeDriverManager().install()
    return chromeDriver
def getFirefoxDriver():
    firefoxDriver = GeckoDriverManager().install()
    return firefoxDriver
def getOperaDriver():
    operaDriver = OperaDriverManager().install()
    return operaDriver