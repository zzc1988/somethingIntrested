#!/usr/bin/env python3
#-*- coding: utf-8 -*-


from bs4 import BeautifulSoup
import re
from urllib import request
from collections import deque
from urllib.request import urlopen
import time
import random

def get_pic (url = "",path = "",i=0):
    pic_deque = deque()
    url = request.Request(url,headers={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:47.0) Gecko/20100101 Firefox/47.0'})
    data = BeautifulSoup(urlopen(url),'html.parser')
    for x in data.findAll('img', {'src' : re.compile("^(http://(.*)\.sinaimg\.(.*)\.jpg$)")}):
        x = x.attrs["src"]          #attribute
        pic_deque.append(x)
    print("start")
    while len(pic_deque) > 0:
        try:
            f = open(path + '/' + str(i) + '.jpg','wb')
            img = pic_deque.popleft()
            img = request.Request(img,headers={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:46.0) Gecko/20100101 Firefox/47.0'})
            img = urlopen(img)
            a = img.read()
            f.write(a)
            print('get------>pic'+str(i))
            i+=1
            time.sleep(random.randint(3,15))
        except:
            continue;



get_pic('http://jandan.net/ooxx/page-2039#comments','/Users/zhangzhichao/Documents/pic')




#http://jandan.net/ooxx/page-2024#comments

