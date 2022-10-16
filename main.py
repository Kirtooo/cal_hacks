from ppp import time_Generator
from schedule import get_result
def main():
    base = {}
    seasonList = ['fall', 'spring', 'summer']
    semester = input("please input semester(E.g. Fall-2022): ")
    if semester == 'quit':
        return None
    while not(('-' in semester) and ((((semester.split('-'))[0]).lower()) in seasonList) and (((semester.split("-"))[1]).isnumeric())):
        semester = input("WRONG FORMAT! Please input semester again (E.g. Fall-2022): ")
        if semester == 'quit':
            return None
    group_num = int(input("Please input the total number of group you want to chosose: "))
    course_choose = []
    result = []
    for i in range(group_num):
        print('\n' + "Group" + str(i + 1))
        class_num = int(input("Please input the total number of courses you want to have in this group: "))
        select_num = int(input("Please input the number of courses you want to choose from this group: "))
        course_choose.append(select_num)
        courses = {}
        for j in range(0, class_num):
            course = input("please input course " + str(j + 1) + " name(E.g. compsci 61A): ")
            if course == 'quit':
                return None
            while not(' ' in course):
                course = input("WRONG FORMAT! Please input course name again(E.g. compsci 61A): ")
                if course == 'quit':
                    return None
            course_subject = course.split()[0]
            course_index = course.split()[1]
            course_name = course_subject + course_index
            course_time = time_Generator(semester, course_subject, course_index)
            while (course_time == {}):
                inn = input("ATTENTION: the course you input does not exist. Enter y if you want to input the course again: ")
                if inn == 'quit':
                    return None
                if inn == 'y':
                    course = input("please input course " + str(j + 1) + " name(E.g. compsci 61A): again")
                    if course == 'quit':
                        return None
                    while not(' ' in course):
                        course = input("WRONG FORMAT! Please input course " + str(j + 1) + " name again(E.g. compsci 61A): ")
                        if course == 'quit':
                            return None
                    course_subject = course.split()[0]
                    course_index = course.split()[1]
                    course_name = course_subject + course_index
                    course_time = time_Generator(semester, course_subject, course_index)
                else:
                    break
            base[course_name] = course_time
            courses[course_name] = course_time
            result.append(courses)
        print('\n')
    print("Below are the possibly course selection for you: ")
    return get_result(result, course_choose, base)
