import dashscope

# 设置阿里云API密钥
dashscope.api_key = ""

def generate_reply(user_input):
    response_generator = dashscope.Generation.call(
        model='qwen-turbo',
        prompt=user_input,
        stream=True,
        top_p=0.8)

    reply_text = ''
    for resp in response_generator:
        paragraph = resp.output.text
        reply_text = paragraph

    return reply_text
