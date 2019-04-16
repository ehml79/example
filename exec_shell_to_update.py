# bottle框架调用shell脚本，执行更新操作的一个小脚本
#这里需要额外导入 request 方法
from bottle import route, run ,request
import paramiko

hostname = '1.1.1.1'
username = 'root'
password = '123456'

def do_shell():
        # 创建SSH对象
        ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        ssh.connect(hostname=hostname, port=22, username=username, password=password)
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command('/bin/bash  /data/sh/update/rsync_update_scripts.sh')
        # 获取命令结果
        result = stdout.read()
        # 关闭连接
        ssh.close()
        return 0

@route('/')
def submit():
        '''
        这里不指定方法时，默认就是GET方法
        登陆页面，html代码都是直接从这里返回到网页中去的，如果不带任何方法，此函数将响应
        关于模板的使用，后面课程会讲到
        '''
        return '''
        <html>
        <head>
        </head>
        <body>
        <form action="/" method="post">
            <input value="Update" type="submit" />
        </form>
        </body>
        </html>
    '''
@route('/', method='POST')
def do_submit():
        '''
        函数名字随意定，这里是进行POST动作的，所以用了do_login，函数名不能与前后函数有同名
        登陆动作，这里用了post，也就是当访问login页面，同时带了POST请求时，这个函数将响应
        '''
        if do_shell() == 0:
                result = '<b> ok!</b>'
        else:
                result = '<b> something wrong!</b>'
        return result

run(host='0.0.0.0', port=80, debug=True)   #开启服务