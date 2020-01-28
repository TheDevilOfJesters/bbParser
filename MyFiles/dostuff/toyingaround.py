link = "https://blackboard.students.ptcollege.edu/webapps/blackboard/execute/launcher?type=Course&id=_3689_1&url="


print(link)
splitLink = link.split("_", 2)
print(splitLink[1])

classLinkStart = "https://blackboard.students.ptcollege.edu/webapps/blackboard/execute/announcement?method=search&context=course_entry&course_id=_"
classLinkEnd = "_1&handle=announcements_entry&mode=view"
# https://blackboard.students.ptcollege.edu/webapps/blackboard/execute/announcement?method=search&context=course_entry&course_id=_3689_1&handle=announcements_entry&mode=view
# https://blackboard.students.ptcollege.edu/webapps/blackboard/execute/announcement?method=search&context=course_entry&course_id=_3610_1&handle=announcements_entry&mode=view
# https://blackboard.students.ptcollege.edu/webapps/blackboard/execute/announcement?method=search&context=course&course_id=_3360_1&handle=cp_announcements&mode=cpview
