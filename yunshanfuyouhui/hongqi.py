# -*- coding: utf-8 -*-
import requests
import json

def dingmessage(result):
    # 请求的URL，WebHook地址
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=0054ac5c5c48059ef10247852f36f8d08519971d68659e83ff6ee063745c52f3"
    # 构建请求头部
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    # 构建请求数据
    message = {
        "msgtype": "text",
        "text": {
            "content": result
        },
        "at": {

            "isAtAll": True
        }
    }

    # 对请求的数据进行json封装
    message_json = json.dumps(message)
    # 发送请求
    info = requests.post(url=webhook, data=message_json, headers=header)
    # 打印返回的结果
    print(info.text)

url = "https://content.95516.com/koala-pre/koala/shop/coupon?cityCd=511100&shopId=60212"
re = requests.get(url=url)
# print(re.text)
data2 = json.loads(re.text)
print(data2)
if re.json()['resp'] == "00":
    coupons = re.json()['params']['allCoupons']
    for coupon in coupons:
        print(coupon['couponNm'])
        print(coupon['couponQuota'])
        print(coupon['validTime'])
        # print(coupon['couponQuota'])
        # print(coupon['couponQuota'])
        # print(coupon['couponQuota'])
        # print(coupon['couponQuota'])
        # print(coupon['couponQuota'])
    # print(coupons)
