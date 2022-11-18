def get_possibility_helper(course_lst, number_for_choosing, curr_lst):
    if (number_for_choosing == 0 or course_lst == []):
        return [curr_lst]
    else:
        first_course = course_lst[0]
        curr_lst_copy = [ele for ele in curr_lst]
        curr_lst.append(first_course)
        return get_possibility_helper(course_lst[1:], number_for_choosing - 1, curr_lst) + get_possibility_helper(course_lst[1:], number_for_choosing, curr_lst_copy)
        
        
def get_possibility(course_lst, number_for_choosing):
    return get_possibility_helper(course_lst, number_for_choosing, [])

def put_arr_list(list_course, two_d_array, course_dictionary_list):
    lst = []
    for i in range(len(list_course)):
        if (put_arr_course(list_course[i], two_d_array, course_dictionary_list)):
            lst.append(course_dictionary_list[i])
    return lst

def turn_to_list(course_dic):
    lst = []
    for dic in course_dic:
        lst.append(list(dic.keys()))
    return lst

def put_arr_course(course_time, two_d_array, course_dictionary_list):
    for day in [1, 2, 3, 4, 5]:
        if day in course_time:
            for i in range(course_dictionary_list[day][0] * 2 + 1, course_dictionary_list[day][1] * 2 + 1):
                if (two_d_array[day][i] == True):
                    return False
                else:
                    two_d_array[day][i] = True
    return True

def get_result(course_dictionary_list, number_for_choosing):
    course_list = turn_to_list(course_dictionary_list)
    lst = []
    for i in range(len(course_list)):
        lst2 = get_possibility(course_list[i], number_for_choosing[i])
        lst3 = [ele for ele in lst2 if len(ele) == number_for_choosing[i]]
        lst.append(lst3)
    return result_filter(lst, course_dictionary_list)

def result_filter(non_filter_result_list, course_dictionary_list):
    two_d_array = []
    for i in range(5):
        two_d_array.append([])
        for j in range(48):
            two_d_array[i].append(False)
    return put_arr_list(non_filter_result_list, two_d_array, course_dictionary_list)

    
print(get_result([{'compsci61A': {1: (13.0, 14.0), 3: (13.0, 14.0), 5: (13.0, 14.0)}, 'compsci61B': {1: (14.0, 15.0), 3: (14.0, 15.0), 5: (14.0, 15.0)}, 'compsci61C': {1: (10.0, 11.0), 3: (10.0, 11.0), 5: (10.0, 11.0)}}, {'compsci70': {2: (9.5, 11.0), 4: (9.5, 11.0)}, 'compsci161': {1: (18.5, 20.0), 3: (18.5, 20.0)}, 'compsci162': {2: (15.5, 17.0), 4: (15.5, 17.0)}}, {'compsci164': {2: (11.0, 12.5), 4: (11.0, 12.5)}, 'compsci186': {1: (10.0, 11.5), 3: (10.0, 11.5)}, 'compsci188': {2: (17.0, 18.5), 4: (17.0, 18.5)}}], [1, 2, 3]))