import time
from selenium import webdriver


def getClassNames(driver, myvars):
    #    classes = driver.find_elements_by_xpath("/html/body/div[3]/div[3]/div[2]/div/div[3]/div[1]/ul[1]/li")
    classes = driver.find_elements_by_xpath("//*[@id=\"_3_1termCourses_noterm\"]/ul[1]/li/a")
    #classes = driver.find_elements_by_partial_link_text("January")
    # print(len(classes))
    # print(classes[0].text)

    print(len(classes))

    driver.get(getClassLinkID(classes[0].get_attribute("href")))

    getAssginments(driver)

def getClassLinkID(classLink):
    classLinkStart = "https://blackboard.students.ptcollege.edu/webapps/blackboard/execute/announcement?method=search&context=course_entry&course_id=_"
    classLinkEnd = "_1&handle=announcements_entry&mode=view"

    splitLink = classLink.split("_", 2)
    link = classLinkStart + splitLink[1] + classLinkEnd
    # print(link)
    return link


# put classes in a sqlite databse with their course id and url-course id for quick navigation later


def getAssginments(driver):
    assignments = driver.find_elements_by_partial_link_text("Assignments")
    # driver.get(assignments[0].get_attribute("href"))
    print(assignments[0].text)

    driver.get(assignments[0].get_attribute("href"))

    links = driver.find_elements_by_tag_name("a")

    print(len(links))
    print(links[31].text)
    driver = driver.find_element_by_id("content_listContainer")
    newlinks = driver.find_elements_by_tag_name("a")
    print(len(newlinks))
    # print(assignments[0].get_attribute("href"))
    time.sleep(7)
