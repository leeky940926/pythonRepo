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
school_info_url = f"https://open.neis.go.kr/hub/classInfo?KEY={API_KEY}&Type=json&pIndex=1&pSize=100&ATPT_OFCDC_SC_CODE=J10&SD_SCHUL_CODE=7569019"

timetables = requests.get(url=school_info_url)
timetables = timetables.json()
timetables = timetables["classInfo"][1]
timetables = timetables["row"]

data = dict()
data_list = []

# for timetable in timetables:
#     data_list.append(    
#         {data["office_education_code"] = timetable["ATPT_OFCDC_SC_CODE"]
#         data["office_education_name"] = timetable["ATPT_OFCDC_SC_NM"]
#         data["school_code"] = timetable["SD_SCHUL_CODE"]
#         data["school_name"] = timetable["SCHUL_NM"]
#         data["year"] = timetable["AY"]
#         data["grade"] = timetable["GRADE"]
#         data["class"] = timetable["CLASS_NM"]}
)
print(data)