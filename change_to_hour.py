
def change_to_hours(str_time):
    hour = int(str_time[:2])
    min = int(str_time[3:5])
    min += hour * 60
    if (min % 10 == 9):
        min += 1
    return min/60
