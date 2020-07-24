# -*- coding: utf-8 -*-

import requests
import json

url = 'http://api.fir.im/apps/5be4f90f959d69333dd5ab5a/releases/5e0abe8eb2eb464e8f620c3c'
headers ={"accesstoken": "c0f6dc8a7d7704d919cbc5d69e6cb2852d1783a1c9"}



# print type(body)
# print type(json.dumps(body))
# 这里有个细节，如果body需要json形式的话，需要做处理
# 可以是data = json.dumps(body)
response = requests.delete(url, headers = headers)
# # 也可以直接将data字段换成json字段，2.4.3版本之后支持
# # response  = requests.post(url, json = body, headers = headers)
#
# # 返回信息
print response.text
# 返回响应头
print response.status_code