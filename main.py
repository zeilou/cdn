# -*- coding: utf8 -*-
import json
import time
import requests
import re
import json
latest = []
latest_content =''

def init():
    global latest_content
    latest_content = '''
<p align="center"><a href="http://zeilou.meowa.cn/" target="_blank" rel="noopener noreferrer"><img width="100" src="https://zeilou.github.io/jz.jpg" alt="logo"></a></p>

### 网盘资源搜索地址
### [http://ijji.top/U9Nk](http://ijji.top/U9Nk)
### 在线网站地址(浏览器)
### [http://ijji.top/KsRA](http://ijji.top/KsRA)
### 网·购查卷更优惠
### [http://ijji.top/bcnR](http://ijji.top/bcnR)
###  饿了么.饭钱补贴每天领
### [http://t.cn/A6Ljna6h](http://t.cn/A6Ljna6h)
### 美团.随机红包也来了
### [http://ijji.top/9moS](http://ijji.top/9moS)
\n\n\n#### 实时采集记录\n'''

def movie_string(index,movie):
    try:
        movie = movie.replace("提","  提")
        link = re.findall('https?://[^\s]+', movie)[0]
    except Exception as e:
        print('error '+movie)
        print(str(e))
        return '\n'
    return '##### '+str(index) + '.' + movie.replace(link,'[{}]({})'.format(link,link))+'\n'

def start_update():
    global latest,latest_content
    time_now = time.localtime()
    df = '%Y-%m-%d %H:%M:%S'
    time_name = time.strftime(df, time_now)
    latest_content +='最近采集时间:'+time_name+'\n'
    latest = requests.get('https://k2f1.cn/a/last').json()['data']
    for i in range(len(latest)-1):
        latest_content += movie_string(i+1,latest[i])
        
    #with open('最新.txt', 'w', encoding='UTF-8') as f:
     #       f.write(latest_content + '\n')

def post_data():
    global latest_content
    headers = {
        'X-Auth-Token':'NEJ6a7XmcYSDjlNB8piGefgh1b26vTVXLAYmEioy'
    }
    data ={
        'key':'movie',
        'slug':'movie',
        'title':'🌈电影收集爱好者🌈',
        'public':'1',
        'format':'markdown',
        'body': latest_content

    }
    url = 'https://www.yuque.com/api/v2/repos/lingyinziluo/tqghhn/docs/16184159'#16184159
    res = requests.put(url=url,data=data,headers=headers)

init()
start_update()
print(latest_content)
with open('./README.md','w') as f:
  f.write(latest_content)
  f.close()
