import time


def getClassNames(driver, myvars):
    #    classes = driver.find_elements_by_xpath("/html/body/div[3]/div[3]/div[2]/div/div[3]/div[1]/ul[1]/li")
    classes = driver.find_elements_by_xpath("//*[@id=\"_3_1termCourses_noterm\"]/ul[1]/li/a")
    #classes = driver.find_elements_by_partial_link_text("January")
    # print(len(classes))
    # print(classes[1].text)


    splitLink = getClassLinkID(classes[0].get_attribute("href"))

    # print(splitLink)
    driver.get(splitLink)
    getAssginments(driver)

def getClassLinkID(classLink):
    classLinkStart = "https://blackboard.students.ptcollege.edu/webapps/blackboard/execute/announcement?method=search&context=course_entry&course_id=_"
    classLinkEnd = "_1&handle=announcements_entry&mode=view"

    splitLink = classLink.split("_", 2)
    print(splitLink)
    return classLinkStart + splitLink[1] + classLinkEnd


# put classes in a sqlite databse with their course id and url-course id for quick navigation later


def getAssginments(driver):
    assignments = driver.find_elements_by_partial_link_text("Assignments")
    print(assignments)
    # print(assignments[1].text)
    print(assignments[0].get_attribute("href"))
    driver.get(assignments[0].get_attribute("href"))
    time.sleep(5)
#     #https://blackboard.students.ptcollege.edu/webapps/blackboard/content/listContent.jsp?course_id=_3689_1&content_id=_425670_1&mode=reset  -- enterprise apps
#     #<a href="/webapps/blackboard/content/listContent.jsp?course_id=_3689_1&amp;content_id=_425670_1&amp;mode=reset" target="_self"><span title="Weekly Assignments">Weekly Assignments</span></a>   -- enterprise
#     #//*[@id="paletteItem:_84158_1"]/a
#     #/html/body/div[5]/div[2]/nav/div/div[2]/div[1]/div[2]/ul/li[8]/a
#
#     #https://blackboard.students.ptcollege.edu/webapps/blackboard/content/listContent.jsp?course_id=_3610_1&content_id=_420111_1&mode=reset  --effective speech
#     #<a href="/webapps/blackboard/content/listContent.jsp?course_id=_3610_1&amp;content_id=_420111_1&amp;mode=reset" target="_self"><span title="Assignments">Assignments</span></a>   -- speech
#     # //*[@id="paletteItem:_83589_1"]/a
#     #/html/body/div[5]/div[2]/nav/div/div[2]/div/div[2]/ul/li[11]/a