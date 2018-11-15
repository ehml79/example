
# 获取程序执行返回值

from subprocess import Popen,PIPE


p = Popen("cp -rf a/* b/", shell=True, stdout=PIPE, stderr=PIPE)
p.wait()
if p.returncode != 0:
    print("Error")
    # return -1
