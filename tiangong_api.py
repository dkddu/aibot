# -*- coding: utf-8 -*-
import requests
import time
import hashlib
import json

url = 'https://{api.singularity-ai.com}/sky-saas-search/api/v1/search'
app_key = ''        # 这里需要替换你的APIKey
app_secret = ''  # 这里需要替换你的APISecret
timestamp = str(int(time.time()))
sign_content = app_key + app_secret + timestamp
sign_result = hashlib.md5(sign_content.encode('utf-8')).hexdigest()


# 设置请求头，请求的数据格式为json
headers={
    "app_key": app_key,
    "timestamp": timestamp,
    "sign": sign_result,
    "Content-Type": "application/json",
    "stream": "true" # or change to "false" 不处理流式返回内容
}

# 设置请求URL和参数

def generate_reply(user_input):
    data = {
    "messages": [
        {
            "role": "system",
            "content": "你的名字叫做天工AI,是一个智能AI助手"
        },
        {
            "role": "user",
            "content": user_input
        }
    ],
    "model": "SkyChat-MegaVerse"
}
# 发起请求并获取响应
    response = requests.post(url, headers=headers, json=data, stream=True)
# 处理响应流
    for line in response.iter_lines():
        if line:
            reply_text = line.decode('utf-8')
    return reply_text
