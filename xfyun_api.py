import sparkAPI

# 以下密钥信息从控制台获取
appid = "78858893"  # 填写控制台中获取的 APPID 信息
api_secret = "N2E5N2VlMjBkMmU2NTBiYjM5NmQxMWQx"  # 填写控制台中获取的 APISecret 信息
api_key = "5d5b3e5ba5968db0e364a6c470fffaa9"  # 填写控制台中获取的 APIKey 信息

domain = "generalv3.5"  # v3版本
# 云端环境的服务地址
Spark_url = "ws://spark-api.xf-yun.com/v3.5/chat"  # v3环境的地址（"wss://spark-api.xf-yun.com/v3.1/chat）

text = []


# length = 0

def getText(role, content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text


def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length


def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text


def generate_reply(user_input):
    question = checklen(getText("user",user_input))
    sparkAPI.answer = ""
    sparkAPI.main(appid, api_key, api_secret, Spark_url, domain, question)
    text.clear()
    reply_text = sparkAPI.answer
    return reply_text
# if __name__ == '__main__':
#     text.clear
#     while (1):
#         Input = input("\n" + "我:")
#         question = checklen(getText("user", Input))
#         sparkAPI.answer = ""
#         print("星火:", end="")
#         sparkAPI.main(appid, api_key, api_secret, Spark_url, domain, question)
#         getText("assistant",sparkAPI.answer)
#         # print(str(text))
# def spark_api(question):
#     """
#     :param question:
#     :return:
#     """
#
#     question = checklen(getText("user", question))
#     SparkApi.answer = ""
#     SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question)
#     text.clear()
#     return SparkApi.answer