
from uiautomation import WindowControl  # 导入用于控制 Windows 窗口的库
import erniebot  # 导入文心一言库
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
        erniebot.api_type = 'aistudio'
        erniebot.access_token = '08910ec3505c12cbb5b0aa86e6336b275aad0a1b'  # 设置个人的访问令牌
        response = erniebot.ChatCompletion.create(
            model='ernie-3.5',
            messages=[{'role': 'user', 'content': last_msg}],
            system="你是现在是一只可爱的猫娘，回答消息的时候会在前面加上是,主人,并在后面加上喵",
        )  # 使用文心一言进行聊天补全
        wx.SendKeys(response.get_result(), waitTime=5)   # 将聊天补全的结果发送给微信
        wx.SendKeys('{Enter}', waitTime=1)  # 模拟按下回车键
        wx.TextControl(SubName=last_msg[:5]).Click()  # 点击对应的消息