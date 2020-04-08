import time


def login(driver, my_vars):
    username = str(my_vars['uname'])
    password = str(my_vars['passwd'])
    site_base = str(my_vars['siteBase'])
    school_domain = str(my_vars['schoolDomain'])

    url = "http://" + username + ":" + password + "@" + site_base
    driver.get(url)
    username_ele = driver.find_element_by_id("userNameInput")
    username_ele.send_keys(school_domain + username)
    password_ele = driver.find_element_by_id("passwordInput")
    password_ele.send_keys(password)
    password_ele.submit()
    time.sleep(5)
    #print(driver.page_source)

