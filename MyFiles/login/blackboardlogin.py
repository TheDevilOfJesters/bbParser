def login(driver, my_vars):
    username = str(my_vars['uname'])
    password = str(my_vars['passwd'])
    siteBase = str(my_vars['siteBase'])
    schoolDomain = str(my_vars['schoolDomain'])

    URL = "http://" + username + ":" + password + "@" + siteBase
    driver.get(URL)
    usernameEle = driver.find_element_by_id("userNameInput")
    usernameEle.send_keys(schoolDomain + username)
    passwordEle = driver.find_element_by_id("passwordInput")
    passwordEle.send_keys(password)
    passwordEle.submit()
    # print(driver.page_source)
