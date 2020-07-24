# -*- coding: utf-8 -*-
from datetime import datetime
import requests
import json


# 17 8.30 ~ 9
# 18 9 ~ 9.30
# 19 9.30 ~ 10
# 20 10 ~ 10.30
# 21 10.30 ~ 11
# 27 13.30 ~ 14
# 28 14 ~ 14.30
# 29 14.30 ~ 15
# 30 15 ~ 15.30
# 31 15.30 ~ 16

def dingmessage(result):
    # 请求的URL，WebHook地址
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=91dd6bd4681fd2f22cfc757913de373d11d5db56a057e866cbd3e3debffbb8ca"
    # 构建请求头部
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    message = {
        "msgtype": "text",
        "text": {
            "content": result
        },
        "at": {

            "isAtAll": True
        }

    }

    message_json = json.dumps(message)
    # for i in range(1, 2):
    # 发送请求
    info = requests.post(url=webhook, data=message_json, headers=header)
    # 打印返回的结果
    print(info.text)


today = str(datetime.today().date())
print(today)

times = {17: "8:30 - 9:00",18: "9:00 - 9:30",19: "9:30 - 10:00",20: "10:00 - 10:30",21: "10:30 - 11:00",27: "13:30 - 14:00",28: "14:00 - 14:30",29: "14:30 - 15:00",31: "15:00 - 15:30",31: "15:30 - 116:00"}
acceptTimes = [17, 18, 19, 22, 27, 28, 29, 30, 31]
data1 = {
    "hospitalId": 77270,
    "vaccList": "",
    "childCode": "51012320170526000156",
    "birthday": "2017-05-26",
    "timestamp": 1593656684,
    "date": "2020-07-29"
}
data2 = {
    "hospitalId": 77270,
    "vaccList": "",
    "childCode": "51012320170526000156",
    "birthday": "2017-05-26",
    "timestamp": 1593656684,
    "date": "2020-08-05"

}
# data3 = {
#             "hospitalId": 22690,
#             "vaccList": "1801,1902",
#             "childCode": "510115120420180802",
#             "birthday": "2018-06-06",
#             "timestamp": 1593412879,
#             "date": "2020-07-03"
#
#         }
url = 'https://dm.yeemiao.com/appointment/hospitalDetail'
url2 = 'https://dm.yeemiao.com/appointment/makeAppointment'
headers = {"Accept": "*/*",
           "Accept-Encoding": "gzip, deflate, br",
           "Accept-Language": "zh-Hans-CN;q=1",
           # "Connection": "keep-alive",
           # "Content-Length": "571",
           "Content-Type": "application/json;charset=utf-8",
           "Cookie": "acw_tc=2f6a1fe515955698732806942e7e720861e80ded65b8636d6bc745e15f789b; Hm_lvt_842ee79c95ff3ba5c3cfa614ebbdd151=1595312289; mp_vacc-check-web_oi=%7B%22_oi%22%3A%20%22173031a77839cd-0cb8ca280c6421-2c734b26-4a640-173031a7784a6f%22%2C%22__timers%22%3A%20%7B%22check_index_v%22%3A%201593656581465%7D%7D",
           "Host": "dm.yeemiao.com",
           "User-Agent": "yeemiao/5.9.1 (iPhone; iOS 14.0; Scale/3.00);xdm/5.9.1;appBuild/202006101440;iOS/14.0",
           "clientInfo": "{\"appVersion\":\"202006101440\",\"appPlatform\":\"ios\",\"deviceCode\":\"1c522a4fdc0d72ad022130aa48f0de4a06493b05\",\"clientIp\":\"192.168.0.0\",\"channel\":\"AppStore\"}",
           "token": "593383ddceb18a7e835791b7e2791240000022729936"}

def reserve(date, time):
    try:
        resrveJson = {
            "immunityCard": "0055638391",
            "timestamp": 1593497554,
            "refDate": "2020-06-29",
            "date": date,
            "token": "593383ddceb18a7e835791b7e2791240000022729936",
            "extraInfo": {
                "childName": "张宇辰",
                "childGender": 1,
                "userMobile": "18628110086",
                "childId": 22391599,
                "childCode": "510109060120172081",
                "birthday": "2017-05-26"
            },
            "hospitalId": 77270,
            "hh": time,
            "sign": "b8eb1e052ba3bfdc375d9c07d70da035"
        }

        res = requests.post(url=url2, json=resrveJson, headers=headers)
        if res.json()['code'] == "0000":
            dingmessage(date + "疫苗预约成功，jia")
        else:
            dingmessage(res.json()['errorMsg'] + "jia")
    except Exception as e:
        dingmessage("jia%s" % (e))


li = [data1, data2]
for i in li:
    try:
        re = requests.get(url=url, json=i, headers=headers)
        for detail in re.json()["data"]["details"]:
            time = detail["hh"]
            count = detail["odd"]
            print(i["date"] + " " + times[time] + " 剩余数量 " +str(count))
            if time in acceptTimes and count != 0:
                dingmessage(i["date"] + "可以预约疫苗了,jia")
                reserve(i["date"], time)
                break
            else:
                print(times[time] + " 不可预约疫苗,jia")
    except Exception as e:
        dingmessage("jia%s" % (e))
