# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 12:34:28 2021

@author: Administrator
"""

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
import requests  # http客户端
import re  # 正则表达式模块
import random  # 随机数
import os  # 创建文件夹


def mkdir(path):  # 创建文件夹
    is_exists = os.path.exists(path)
    if not is_exists:
        print('创建名字叫做', path, '的文件夹')
        os.makedirs(path)
        print('创建成功！')
    else:
        print(path, '文件夹已经存在了，不再创建')


def getPic(html, keyword, path):
    print("正在查找：" + keyword + ' 对应的图片，正在从百度图库重下载：  ')
    print(html)
    print(re.findall(str('"imgurl":"(.*?)"'), html, re.S))
    for addr in re.findall(str('"imgurl":"(.*?)"'), html, re.S):
        print("现在正在爬取的URL地址：" + addr)
        try:
            pics = requests.get(addr, timeout=10)
        except requests.exceptions.ConnectionError:
            print("当前Url请求错误")
            continue
        # 假设产生的随机数不重复
        fq = open(path + '//' + str(random.randrange(1000, 2000)) + '.jpg', 'w+b')
        fq.write(pics.content)
        fq.close()
        print('写入完成')


if __name__ == "__main__":
    word = input("请输入关键词：")
    result = requests.get("https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CE%E2%C0%DA&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=000000")
    # print(result.text)
    print("写入完毕")
    path = 'E:/PersonRecognitionDlib/Person/person2'  # 保存图片文件夹名称
    mkdir(path)
    getPic(result.text, word, path)
'''
# -*- coding:utf-8 -*-
import os
import requests
import re
from bs4 import BeautifulSoup
# 爬取图片的地址
url = "" # 古装美女
# 获取网页内容
htmls = requests.get(url).text
 
soup = BeautifulSoup(htmls, 'html.parser', from_encoding='utf-8')
#  findall() 全局搜索,搜索到所有img标签的元素
pic_url = soup.find_all('img', src=re.compile(r'^http://t2.hddhhn.com/uploads/tu(.*)jpg$'))
 
i = 0
# 判断images文件夹是否存在，如果不存在，则创建
if not os.path.exists('images'):
    os.makedirs('images')
# 利用for循环遍历图片的地址
for url in pic_url:
    img = url['src']
    try:
        pic = requests.get(img,timeout=5) # 超时异常判断 5秒超时
    except requests.exceptions.ConnectionError:
        print("图片无法下载")
        continue
    file_name = "E:/PersonRecognitionDlib/Person/images/"+ str(i) + ".jpg" # 存储图片的路径及保存的名字
    print(file_name)
 
    fp = open(file_name,'wb+')
    fp.write(pic.content) # 写入图片
    fp.close() # 关闭
    i += 1



