import json
import requests

#초등학교
ele_url = "https://search.map.kakao.com/mapsearch/map.daum?callback=jQuery181019095482702476918_1650701497825&q=%EC%B4%88%EB%93%B1%ED%95%99%EA%B5%90&msFlag=A&sort=0&page=1"

WEBID="a4eedddc5ef246c394f8ef115c944dfb"
WEBID_TS=1630334357359
KDT="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkZXZlbG9wZXJJZCI6MTU4ODI5MywiYWNjb3VudElkIjoxNjMxMzgwNzYsImVtYWlsIjoibGt5b25nMDkyNkBuYXZlci5jb20iLCJ0b2tlbiI6IjRiNTZjZGY0MDJhNTk4Y2EyYzM5NjA4ODJmYTdhOGY3ZGNlYjVjMWFhNDgyZTc4MjQwZjM0NTU0ZjQ2MTU4ZDkifQ.IlCWsjVV_V7hoqTeTwQA_t-yqVVCpk8zFIplNlU_tJI; __T_=1"
TANO="mZstqRvZ/27SR8qTR2ge+BlkS7mQ76xEABEy3R2r3pzW5VKuwGpefE/lUwm6MbftPGIfJUpmUvMRELs37DmWpsrSiTiY/vNrGGesgqQCIAfDRGejT803ZsORuVZKYd6D4V9lgCnDeWfoYPcsCIPgzqWcgtYIRRv/nykqi5SbaEs856JLnsxnznSdw9GfBjXgR5ZfCycRyeVRVsA9Gx2SqdAWBC5ADbL5FxnkRdibKXcUjpkCqAYPlU9SXmM2hesdpeqYxtTqXCT00hHGkCmtB7RkyGLZu2ybNAuemUnvS+4ksIDqp2RJL+6f5nfaZ+t4WwVCVfmO8KeuvRULe0XDtQ=="

ele_headers = {
    "authority": "search.map.kakao.com",
    "scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "cookie": f"webid={WEBID}; webid_ts={WEBID_TS}; _kdt={KDT};_T_ANO={TANO}",
}

params = {
    "callback": "jQuery181019095482702476918_1650701497825",
    "q": "초등학교",
    "msFlag": "A",
    'sort': "0"
}

results = requests.get(url=ele_url, headers=ele_headers).next

print(results)