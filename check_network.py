#!/usr/bin/env python3

# 测试网络

import urllib.request

url =  'https://www.baidu.com/'


try:
    urllib.request.urlopen(url)
    print ("working connection")
except urllib.error.URLError:
    print("No internet connection")
