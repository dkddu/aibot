from uiautomation import WindowControl
import dashscope
import erniebot
import timerun

# 设置阿里云API密钥
dashscope.api_key = ""

# 设置文心一言API访问令牌
erniebot.api_type = 'aistudio'
erniebot.access_token = ''

wx = WindowControl(Name='微信', searchDepth=1)  # 绑定微信主窗口
wx.ListControl()  # 切换窗口
wx.SwitchToThisWindow()  # 切换到微信窗口
hw = wx.ListControl(Name='会话')  # 寻找会话控件绑定

# 默认使用通义千问模型
current_model = 'qwen'

while True:  # 持续接收消息
    we = hw.TextControl(searchDepth=4)  # 查找未读信息
    while not we.Exists():
        pass
    if we.Name:  # 如果存在未读消息
        we.Click(simulateMove=False)  # 点击未读消息
        last_msg = wx.ListControl(Name='消息').GetChildren()[-1].Name  # 读取最后一条消息

        # 判断是否需要切换模型
        if last_msg.strip() == '切换模型':
            current_model = 'ernie' if current_model == 'qwen' else 'qwen'
            reply_text = '切换成功'
        else:
            # 根据当前模型生成回复
            if current_model == 'qwen':
                response_generator = dashscope.Generation.call(
                    model='qwen-turbo',
                    prompt=last_msg,
                    stream=True,
                    top_p=0.8)

                reply_text = ''
                for resp in response_generator:
                    paragraph = resp.output.text
                    reply_text = paragraph
            else:
                response = erniebot.ChatCompletion.create(
                    model='ernie-3.5',
                    messages=[{'role': 'user', 'content': last_msg}],
                    system="你是现在是一只可爱的猫娘，回答消息的时候会在前面加上是,主人,并在后面加上喵",
                )
                reply_text = response.get_result()

        wx.SendKeys(reply_text, waitTime=5)  # 将回复发送给微信
        wx.SendKeys('{Enter}', waitTime=1)  # 模拟按下回车键
        wx.TextControl(SubName=last_msg[:5]).Click()  # 点击对应的消息
        time.sleep(1)  # 设置延时防止频繁调用API
