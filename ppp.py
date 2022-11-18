import requests
from change_to_hour import change_to_hours
def time_Generator(semester, course_subject, course_index):
    sList = semester.split("-")
    season = sList[0]
    year = sList[1]
    url = 'https://classes.berkeley.edu/content/' + year + '-' + season + '-' + course_subject + '-' + course_index + '-001-lec-001'
    #url = 'https://classes.berkeley.edu/content/2022-fall-compsci-61a-001-lec-001'
    html = requests.get(url)
    tex = html.text
    #print(tex)
    meetdays = ["meetsMonday", "meetsTuesday", "meetsWednesday", "meetsThursday", "meetsFriday"]
    days = [1, 2, 3, 4, 5]
    result = {}
    for i in range(5):
        index = tex.find(meetdays[i])
        tex = tex[index: ]
        #print(tex[index + len(meetdays[i]) + 2 : index + len(meetdays[i]) + 6])
        if tex[len(meetdays[i]) + 2 : len(meetdays[i]) + 6] == "true":
            st = tex.find("startTime")
            sth = change_to_hours(tex[st+12: st+22])
            et = tex.find("endTime")
            eth = change_to_hours(tex[et+10: et+19])
            time = (sth, eth)
            result[days[i]] = time

    i = tex.find("meetsFriday") + 17
    z = tex[i:]
    # k = z.find("meetsFriday")
    # print(z[k + 13 : k + 17])
    for j in range(5):
        index = z.find(meetdays[j])
        z = z[index: ]
        # print(z[index + len(meetdays[j]) + 2 : index + len(meetdays[j]) + 6])
        if z[len(meetdays[j]) + 2 : len(meetdays[j]) + 6] == "true":
            st = z.find("startTime")
            sth = change_to_hours(z[st+12: st+22])
            et = z.find("endTime")
            eth = change_to_hours(z[et+10: et+19])
            time = (sth, eth)
            result[days[j]] = time

    return result
