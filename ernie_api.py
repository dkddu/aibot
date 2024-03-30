import erniebot

# 设置文心一言API访问令牌
erniebot.api_type = 'aistudio'
erniebot.access_token = '08910ec3505c12cbb5b0aa86e6336b275aad0a1b'


def generate_reply(user_input):
    response = erniebot.ChatCompletion.create(
        model='ernie-3.5',
        messages=[{'role': 'user', 'content': user_input}],
        system="你是现在是一只可爱的猫娘，回答消息的时候会在前面加上是,主人,并在后面加上喵",
    )
    reply_text = response.get_result()
    return reply_text