
# 读取proto 文件中的某些数据，存入csv


import csv

def readFileName(filename):
    with open(filename,'r',encoding='utf-8') as f:
        data = f.readlines()
        data_all = []
        for i, x in enumerate(data):
            if '协议号' in x:
                protoNum = x[7:12:1]
                desc = data[i - 1][3:].strip('\n')
                name =  data[i + 2][8:].strip('\n')
                data_list = (protoNum,name,desc)
                data_all.append(data_list)
        return data_all


def writeDataToFile(data):
    headers = ['协议号','名称','描述']
    rows = data
    with open('d:\Desktop\stocks.csv','w',encoding='gbk') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)


if __name__ == '__main__':

    filename = 'd:\Desktop\pb_10.proto'
    writeDataToFile(readFileName(filename))
