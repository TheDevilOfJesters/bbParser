import time
from selenium.common.exceptions import NoSuchElementException
from setup.localSetup import create_folder


def getClassNames(driver, myvars):
    # classes = driver.find_elements_by_xpath("//*[@id=\"_3_1termCourses_noterm\"]/ul[1]/li/a")
    table = driver.find_element_by_id("_3_1termCourses_noterm")

    class_list = table.find_elements_by_tag_name("ul")
    classes = class_list[0].find_elements_by_tag_name("li")
    print(len(classes))
    print(classes[0].text)
    for index, item in enumerate(classes):
        class_link = classes[index].find_element_by_tag_name("a")
        if "announcement" not in class_link.get_attribute("href"):
            create_folder(class_link.text, myvars)
    # # classLink = classes[0].find_element_by_tag_name("a")
    # driver.get(getClassLinkID(classLink.get_attribute("href")))
    # # driver.get(getClassLinkID(classes[0].get_attribute("href")))
    class_link = classes[0].find_element_by_tag_name("a")
    driver.get(getClassLinkID(class_link.get_attribute("href")))

    # getAssignments(driver)


def getClassLinkID(class_link):
    class_link_start = "https://blackboard.students.ptcollege.edu/webapps/blackboard/execute/announcement?method" \
                       "=search&context=course_entry&course_id=_ "
    class_link_end = "_1&handle=announcements_entry&mode=view"

    split_link = class_link.split("_", 2)
    link = class_link_start + split_link[1] + class_link_end
    # print(link)
    return link


def getAssignments(driver):
    assignments = driver.find_elements_by_partial_link_text("Assignments")
    driver.get(assignments[0].get_attribute("href"))

    driver = driver.find_element_by_id("content_listContainer")
    driver = driver.find_elements_by_tag_name("li")
    title = driver[1].find_element_by_tag_name("h3")
    try:
        link = title.find_element_by_tag_name("a").get_attribute("href")
        if "app/link/launch" in link:
            print("Going to External Site")
        else:
            print("Error" + link)
    except NoSuchElementException:
        print("Element Does not exist")

    # print(title.text)

    details = driver[0].find_element_by_class_name("details")
    # detailText = str.split(details, "")
    # print(str.strip(details.text))

    time.sleep(7)