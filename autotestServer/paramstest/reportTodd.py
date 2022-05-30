# -*- coding: utf-8 -*-
# author:lixiaoguo
# company:pinpianyi
# createdate:2020/9/25 14:48

"""
环境
pip install DingtalkChatbot
pip install -U DingtalkChatbot

地址
https://github.com/zhuifengshen/DingtalkChatbot

使用场景;
https://blog.csdn.net/zhuifengshenku/article/details/79147479
"""

from dingtalkchatbot.chatbot import DingtalkChatbot


class send_msg():
    def __init__(self,
                 webhook="https://oapi.dingtalk.com/robot/send?access_token=d420e168fe54b6269b616a5c85d770ab1e23295933ff65f73ec92c5f5f06d4a3",
                 secret='自动化测试'):
        # WebHook地址
        # 自定义关键字，发送消息必带
        self.webhook = webhook
        self.secret = secret  # 可选：创建机器人勾选“加签”选项时使用

    # msg：需要发送的消息
    # user：手机号或者钉钉id，作为@指定人，不设置@所有人
    def send_text(self, msg, user=None):
        # 初始化机器人小丁
        # xiaoding = DingtalkChatbot(self.webhook)  # 方式一：通常初始化方式
        xiaoding = DingtalkChatbot(self.webhook, secret=self.secret)  # 方式二：勾选“加签”选项时使用（v1.5以上新功能）
        # xiaoding = DingtalkChatbot(self.webhook, pc_slide=True)  # 方式三：设置消息链接在PC端侧边栏打开（v1.5以上新功能）

        # Text消息@所有人
        if not user:
            r = xiaoding.send_text(msg=self.secret + msg, is_at_all=True)
        else:
            # Text消息之@指定用户
            at_mobiles = [user]
            r = xiaoding.send_text(msg=self.secret + msg, at_mobiles=at_mobiles)
        if ("errcode" in r.keys()) and ("errmsg" in r.keys()):
            if r["errcode"] == 0 and r["errmsg"] == 'ok':
                return {"status": True, "msg": "发送成功"}
            else:
                return {"status": False, "msg": r}
        else:
            print(r)
            if r["statu"] == 1111:
                return {"status": False, "msg": "1分钟内消息超过20条"}

    def send_link(self, title, text, message_url, pic_url=''):
        # Link消息
        xiaoding = DingtalkChatbot(self.webhook, secret=self.secret)  # 方式二：勾选“加签”选项时使用（v1.5以上新功能）
        # xiaoding.send_link(title='万万没想到，某小璐竟然...', text='故事是这样子的...', message_url='http://www.kwongwah.com.my/?p=454748", pic_url="https://pbs.twimg.com/media/CEwj7EDWgAE5eIF.jpg')
        r = xiaoding.send_link(title=self.secret + title, text=text, message_url=message_url, pic_url=pic_url)
        if r["errcode"] == 0 and r["errmsg"] == 'ok':
            return {"status": True, "msg": "发送成功"}
        else:
            return {"status": False, "msg": r}


###  示例
'''
# 群地址
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=d420e168fe54b6269b616a5c85d770ab1e23295933ff65f73ec92c5f5f06d4a3'
# 关键字
secret = 'Hi:'
# send_msg(webhook, secret).send_text("测试结果汇报功能测试", "13362140179")
# send_msg(webhook, secret).send_link('标题',"hahaha","https://blog.csdn.net/zhuifengshenku/article/details/79147479", "https://images.pinpianyi.com/images/supplier/contact_9_1.jpg")
send_msg(webhook, secret).send_link('标题', "hahaha", "https://blog.csdn.net/zhuifengshenku/article/details/79147479")

'''
