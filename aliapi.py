from uiautomation import WindowControl
import dashscope
import time

# 设置阿里云API密钥
dashscope.api_key = ""

wx = WindowControl(Name='微信', searchDepth=1)  # 绑定微信主窗口
wx.ListControl()  # 切换窗口
wx.SwitchToThisWindow()  # 切换到微信窗口
hw = wx.ListControl(Name='会话')  # 寻找会话控件绑定

while True:  # 持续接收消息
    we = hw.TextControl(searchDepth=4)  # 查找未读信息
    while not we.Exists():
        pass
    if we.Name:  # 如果存在未读消息
        we.Click(simulateMove=False)  # 点击未读消息
        last_msg = wx.ListControl(Name='消息').GetChildren()[-1].Name  # 读取最后一条消息
        # 使用通义千问API生成回复
        # ... 其他代码保持不变 ...
        response_generator = dashscope.Generation.call(
            model='qwen-turbo',
            prompt=last_msg,
            stream=True,
            top_p=0.8)
        reply_text = ''
        for resp in response_generator:
            # 从resp.output.text中获取生成的文本
            paragraph = resp.output.text
            reply_text = paragraph
        # ... 其他代码保持不变 ...

        wx.SendKeys(reply_text, waitTime=5)  # 将回复发送给微信
        wx.SendKeys('{Enter}', waitTime=1)  # 模拟按下回车键
        wx.TextControl(SubName=last_msg[:5]).Click()  # 点击对应的消息
        time.sleep(1)  # 设置延时防止频繁调用API
