import itertools
def get_possibility_helper(course_dic, number_for_choosing):
    ks = course_dic.keys()
    return list(itertools.combinations(ks, number_for_choosing))

def get_possibility(course_dic, number_for_choosing):
    result = []
    for i in range(len(number_for_choosing)):
        result.append(get_possibility_helper(course_dic[i], number_for_choosing[i]))
    result = list(itertools.product(*result))
    result = [[element for tupl in tupleOfTuples for element in tupl] for tupleOfTuples in result]
    return result

def put_arr_list(list_course, two_d_array):
    for course in list_course:
        if (not put_arr_course(course, two_d_array)):
            return False
    return True

def put_arr_course(non_filter_result_list, base):
    for i in range(len(non_filter_result_list)):
        two_d_array = result_filter()
        for j in non_filter_result_list[i]:
            time = base[j]
            for day in [1, 2, 3, 4, 5]:
                if day in time.keys():
                    # print(day)
                    for k in range(int(time[day][0] * 2 + 1), int(time[day][1] * 2 + 1)):
                        if (two_d_array[day][k] == True):
                            non_filter_result_list.pop(i)
                            # print("yessss")
                        else:
                            two_d_array[day][k] == True
                            # print("fuckkk")

    return non_filter_result_list

def get_result(course_dictionary_list, number_for_choosing, base):
    lst = get_possibility(course_dictionary_list, number_for_choosing)
    return put_arr_course(lst, base)

def result_filter():
    two_d_array = []
    for i in range(5):
        two_d_array.append([])
        for j in range(48):
            two_d_array[i].append(False)
    return two_d_array
