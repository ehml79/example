import itchat

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])

itchat.auto_login(hotReload=True)
# itchat.send(u'测试消息发送','filehelper')

friends = itchat.get_friends()
print(friends)


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


