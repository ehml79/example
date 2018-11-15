# 清除本地目录结构
# 获取服务器目录结构
# 创建本地目录结构

import paramiko
import os
import time


# for 循环读取所有远程服务器
def for_read_hosts(local_dir, remote_dir):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostip, username=username, password=password)
    ftp = paramiko.Transport(hostip, port)
    ftp.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(ftp)

    dir_list = get_remote_dir_struc(ssh,remote_dir)
    makedir_on_wondows(dir_list)


# 获取服务器目录结构
def get_remote_dir_struc(ssh,remote_dir):
    dir_list = []
    cmd  = 'find ' + remote_dir + ' -type d'
    stdin, stdout, stderr = ssh.exec_command(cmd)
    # 去除以.开头的隐藏目录
    for i in stdout:
        if r'/.' not in i.strip():
            dir_list.append(i.strip())
    return dir_list

# 删除本地目录
def remove_dir(dir):
    dir = dir.replace('\\', '/')
    if(os.path.isdir(dir)):
        for p in os.listdir(dir):
            remove_dir(os.path.join(dir,p))
        if(os.path.exists(dir)):
            try:
                os.rmdir(dir)
            except:
                pass
    else:
        if(os.path.exists(dir)):
            os.remove(dir)

# 创建本地目录
def makedir_on_wondows(dir_list):
    for i in dir_list:
        dir = local_dir +  i
        # print(dir)
        try:
            os.makedirs(dir)
        except:
            pass

if __name__ == '__main__':
    port = 22
    hostip = '192.168.47.22'
    username = 'root'
    password = 'redhat'

    local_dir = 'D:/Desktop/update_dir'
    remote_dir = '/data/app1'

    remove_dir(r'd:/Desktop/update_dir/data')
    for_read_hosts(local_dir, remote_dir)

