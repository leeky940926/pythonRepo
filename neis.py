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

data_list = [
    {
        "semester" : timetable["SEM"],
        "grade" : timetable["GRADE"],
        "class" : timetable["CLASS_NM"],
        "perio" : timetable["PERIO"],
        "subject" : timetable["ITRT_CNTNT"]
    } for timetable in timetables
]

data = {
    "official_education_code" : official_education_code,
    "official_education_name" : official_education_name,
    "school_code" : school_code,
    "school_name" : school_name,
    "year" : year,
    "timetables" : data_list   
}

#급식 
meal_url = f"https://open.neis.go.kr/hub/mealServiceDietInfo?KEY={API_KEY}&Type=json&pIndex=1&pSize=100&ATPT_OFCDC_SC_CODE=J10&SD_SCHUL_CODE=7569019"

meals = requests.get(url=meal_url)
meals = meals.json()["mealServiceDietInfo"][1]
meals = meals["row"]
meals = [
    {
        "meal_name" : meal["DDISH_NM"],
        "origin" : meal["ORPLC_INFO"],
        "calories" : meal["CAL_INFO"],
        "nut_info" : meal["NTR_INFO"]
    } for meal in meals]

