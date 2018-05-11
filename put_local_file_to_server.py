# 
#
#
import os.path
import paramiko
import time


# 读取所有远程服务器
def read_hosts(local_dir, remote_dir):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostip, username=username, password=password)

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


# 遍历文件，找出待上传文件
def get_upload_file(local_path):
    all_file = []
    for parent,dirnames,filenames in os.walk(local_path):
        if  filenames:
            all_file.append(os.path.join(parent,filenames[0]).replace('\\','/'))
    # print(all_file)
    return all_file

# 上传文件
def sftp_file(all_file,host,username,password,):

    username = username
    password = password
    host = host
    port = 22

    t = paramiko.Transport(host,port)
    t.connect(username=username,password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    for localFile in all_file:
        uploadFile = localFile.split(local_dir)[-1]
        print('Put file ... {} To {}'.format(localFile,uploadFile))
        sftp.put(localFile,uploadFile)  #上传文件
    sftp.close()
    t.close()
    print('wait 3s')
    time.sleep(3)



if __name__ == '__main__':

    port = 22
    hostip = '192.168.47.22'
    username = 'root'
    password = 'redhat'

    local_dir = 'D:/Desktop/update_dir'
    remote_dir = '/data/app1'

    all_file = get_upload_file(local_dir)
    sftp_file(all_file,hostip, username,password)

    remove_dir(r'd:/Desktop/update_dir/data')
    read_hosts(local_dir, remote_dir)





