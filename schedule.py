def get_possibility_helper(course_lst, number_for_choosing, curr_lst):
    if number_for_choosing == 0 or not course_lst:
        return curr_lst
    else:
        new_course = course_lst.popitem()
        new_course = {new_course[0] : new_course[1]}
        curr_dic_copy = curr_lst.copy()
        curr_lst.update(new_course)
        with_curr_course = get_possibility_helper(course_lst, number_for_choosing - 1, curr_lst)
        without_curr_course = get_possibility_helper(course_lst, number_for_choosing, curr_dic_copy)
        with_curr_course.update(without_curr_course)
        return with_curr_course

def get_possibility(course_lst, number_for_choosing):
    return get_possibility_helper(course_lst, number_for_choosing, {})

def put_arr_list(list_course, two_d_array):
    for course in list_course:
        if (not put_arr_course(course, two_d_array)):
            return False
    return True

def turn_to_list(course_dic):
    lst = []
    for dic in course_dic:
        lst.append(list(dic.keys()))
    return lst

def put_arr_course(course_time, two_d_array):
    for day in [1, 2, 3, 4, 5]:
        if day in course_time:
            for i in range(course_time[day][0] * 2 + 1, course_time[day][1] * 2 + 1):
                if (two_d_array[day][i] == True):
                    return False
                else:
                    two_d_array[day][i] = True
    return True

def get_result(course_dictionary_list, number_for_choosing):
    lst = []
    for i in range(len(course_dictionary_list)):
        lst.append(get_possibility(course_dictionary_list[i], number_for_choosing[i]))
    return result_filter(lst)

def result_filter(non_filter_result_list):
    two_d_array = []
    for i in range(5):
        two_d_array.append([])
        for j in range(48):
            two_d_array[i].append(False)
    return put_arr_course(non_filter_result_list, two_d_array)
