# 获取所有微信好友头像
import itchat
import os
import PIL.Image as Image

try:
    os.mkdir('D:/imgs')
except:
    pass

# 打印输出信息
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])

# 图片二维码
itchat.auto_login(hotReload=True)

# 字符串二维码
# itchat.auto_login(enableCmdQR=True)


# itchat.send(u'测试消息发送','filehelper')

friends = itchat.get_friends()
print(friends)

# 获取所有微信好友头像

friends = itchat.get_friends(update=True)[0:]
user = friends[0]["UserName"]

num = 0
for i in friends:
    img = itchat.get_head_img(userName=i["UserName"])
    fileImage = open(r'D:/imgs' + "/" + str(num) + ".jpg",'wb')
    fileImage.write(img)
    fileImage.close()
    num += 1


itchat.run()
