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
    print(message)
    message_json = json.dumps(message)
    # for i in range(1, 2):
    # 发送请求
    info = requests.post(url=webhook, data=message_json, headers=header)
    # 打印返回的结果
    print(info.text)


today = str(datetime.today().date())
print(today)

times = {17: "8:30 - 9:00",18: "9:00 - 9:30",19: "9:30 - 10:00",20: "10:00 - 10:30",21: "10:30 - 11:00",27: "13:30 - 14:00",28: "14:00 - 14:30",29: "14:30 - 15:00",30: "15:00 - 15:30",31: "15:30 - 16:00"}
acceptTimes = [16,17,18,19,20,21,27,28,29,30,31]
data1 = {
  "hospitalId": 66721,
  "timestamp": 1596165259,
  "childCode": "511721010520192490",
  "birthday": "2019-12-03",
  "date": "2020-08-06",
  "sign": "47d08df8f9bf986ce67d96f77dfe8694"
}
# data2 = {
#       "hospitalId": 66721,
#   "timestamp": 1596165259,
#   "childCode": "511721010520192490",
#   "birthday": "2019-12-03",
#   "date": "2020-08-03",
#   "sign": "47d08df8f9bf986ce67d96f77dfe8694"
#
# }
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
           "Cookie": "acw_tc=2f6a1fb815961642508047175e5a309badc8739ef2f6b212a17f1e78b9b56c",
           "Host": "dm.yeemiao.com",
           "User-Agent": "yeemiao/5.9.1 (iPhone; iOS 14.0; Scale/3.00);xdm/5.9.1;appBuild/202006101440;iOS/14.0",
           "clientInfo": "{\"appVersion\":\"202006101440\",\"appPlatform\":\"ios\",\"deviceCode\":\"1c522a4fdc0d72ad022130aa48f0de4a06493b05\",\"clientIp\":\"192.168.0.0\",\"channel\":\"AppStore\"}",
           "token": "ee2b10081e34a3c5a702db592551119b000022935511"}

def reserve(date, time):
    try:
        resrveJson = {
  "refstr": "",
  "hh": 18,
  "timestamp": 1596165266,
  "date": "2020-08-06",
  "token": "ee2b10081e34a3c5a702db592551119b000022935511",
  "extraInfo": {
    "childName": "张艳梅之子",
    "childGender": 1,
    "userMobile": "15802880556",
    "childId": 22611934,
    "childCode": "511721010520192490",
    "birthday": "2019-12-03"
  },
  "hospitalId": 66721,
  "immunityCard": "0067122804",
  "sign": "0a11d49ff4de4d3cd2272145f25a88cd"
}

        res = requests.post(url=url2, json=resrveJson, headers=headers)
        print("预约结果 >>>>" + str(res.json()))
        if res.json()['code'] == "0000":
            dingmessage(date + "疫苗预约成功，jia")
        else:
            dingmessage(res.json()['errorMsg'] + "jia")
    except Exception as e:
        dingmessage("jia%s" % (e))

# reserve("2018-08-06", 18)
li = [data1]
for i in li:
    try:
        re = requests.get(url=url, json=i, headers=headers)
        print("查询结果 >>> " + str(re.json()))
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
        print(e)
        dingmessage("jia%s" % (e))
