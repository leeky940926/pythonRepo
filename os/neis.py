from time import time
import requests

API_KEY = "58903d98c8914f0d99132381ce09ec06"

#학교정보
school_info_url = f"https://open.neis.go.kr/hub/schoolInfo?KEY={API_KEY}&Type=json&pIndex=1&pSize=100&ATPT_OFCDC_SC_CODE=J10&SD_SCHUL_CODE=7569019"

school_info = requests.get(url=school_info_url)
school_info = school_info.json()
school_info = school_info["schoolInfo"][1]
school_info = school_info["row"][0]

#학교시간표
school_info_url = f"https://open.neis.go.kr/hub/elsTimetable?KEY={API_KEY}&Type=json&pIndex=1&pSize=100&ATPT_OFCDC_SC_CODE=J10&SD_SCHUL_CODE=7569019"

timetables = requests.get(url=school_info_url)
timetables = timetables.json()
timetables = timetables["elsTimetable"][1]
timetables = timetables["row"]

official_education_code = timetables[0]["ATPT_OFCDC_SC_CODE"]
official_education_name = timetables[0]["ATPT_OFCDC_SC_NM"]
school_code = timetables[0]["SD_SCHUL_CODE"]
school_name = timetables[0]["SCHUL_NM"]
year = timetables[0]["AY"]

data_list = []

for timetable in timetables:
    data_list.append(
        {
            "semester" : timetable["SEM"],
            "grade" : timetable["GRADE"],
            "class" : timetable["CLASS_NM"],
            "perio" : timetable["PERIO"],
            "subject" : timetable["ITRT_CNTNT"]
        }
    )

data = {
    "official_education_code" : official_education_code,
    "official_education_name" : official_education_name,
    "school_code" : school_code,
    "school_name" : school_name,
    "year" : year,
    "timetables" : data_list   
}

print(data)