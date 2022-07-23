import illusts
import json
import time
import os

Settings_text='''{
    "Notes1": "请在此处填入Pixiv站点登录后的Cookie（外带双引号），自行百度如何获取网站cookie",
    "Notes2": "可以为保持如下的原状，但无法爬取R18/R18G图片",
    "cookie": "",
   
    "Notes3": "请在此填入爬取对象的ID，可在其主页查看",
    "Notes4": "必填",
    "PID": 1919810,

    "Notes5":"超时时间，越短越容易进入一直超时的死循环，但会加快速度",
    "Notes6":"第一个为查询url时的，第二个为下载图片时的，一般建议保留原状",
    "Timeout_url":2,
    "Timeout_artworks":10,
    
    "Notes7": "是否开启代理？（没钱用专门的国外http代理池，所以使用 Clash for windows 加 廉价机场 实现）",
    "Notes8": "开启填true 关闭填false",
    "Proxy": false,
    
    "Notes9": "Clash 端口号（可在 Clash-主页-Clash核心版本 条目的右侧查看）",
    "Notes10": "开启代理时必填，关闭时随意",
    "Port": 114514,
    
    "Notes11": "Clash 代理组名称 （可在 Clash-代理 中查看）",
    "Notes12": "开启代理时必填，关闭时随意",
    "Name": "速打游",
    
    "Notes13": "代理组大小 （每爬取多少次更换代理节点）",
    "Notes14": "开启代理时必填，关闭时随意",
    "Batch": 5,
    
    "Notes15": "指定节点范围，第一次使用时会将所有节点都打印出来，可以从中复制出来",
    "Notes16": "不需要指定时请直接填null（不带[]），否则可能会出现无法自动选择代理节点的错误",
    "Order": ["G 香港1", "G 香港2", "G 香港3", "G 台湾1", "G 日本1", "S 日本1"]
}'''
if not os.path.isfile ('Settings.json'):
    with open('Settings.json','w',encoding='utf-8') as fb:
        fb.write(Settings_text)
    print('Please read the "Settings.json" file that appears below and fill it out')
    input('press Enter to exit')
    exit()

Start = time.time()

with open('Settings.json', 'r', encoding='utf-8') as fp:
    Settings = json.load(fp)

print('Loading cookie...')
Photo = illusts.Pixiv_illusts(Settings['cookie'])
print('done')
time.sleep(0.5)

if Settings['Proxy']:
    print('Loading proxies...')
    Photo.Get_Proxies(Settings['Port'], Settings['Name'])
    print('done')
    time.sleep(0.5)

print('Geting illusts...')
Photo.Get_illusts(Settings['PID'])
print('done')
time.sleep(0.5)

if not Settings['Proxy']:
    print('Geting urls...')
    Photo.Get_urls(Settings['Timeout_url'])
    print('done')
    time.sleep(0.5)
    print('Geting Artworks')
    Photo.Get_artworks(Settings['Timeout_artworks'])
    print('done')
    time.sleep(0.5)
    End = time.time()
    print('use: ' + str(End - Start)+'s')
    input('press Enter to exit')
    exit()
elif not type(Settings['Order']) == list:
    print('Geting urls with proxy...')
    Photo.Get_urls_With_Proxy(Settings['Batch'], Settings['Timeout_url'])
    print('done')
    time.sleep(0.5)
    print('Geting Artworks with proxy')
    Photo.Get_artworks_With_Proxy(
        Settings['Batch'], Settings['Timeout_artworks'])
    print('done')
    time.sleep(0.5)
    End = time.time()
    print('use: ' + str(End - Start)+'s')
    input('press Enter to exit')
    exit()

else:
    print('Geting urls with ordered proxy...')
    Photo.Get_urls_With_Proxy_Order(
        Settings['Batch'], Settings['Order'], Settings['Timeout_url'])
    print('done')
    time.sleep(0.5)
    print('Geting Artworks with ordered proxy')
    Photo.Get_artworks_With_Proxy_Order(
        Settings['Batch'], Settings['Order'], Settings['Timeout_artworks'])
    print('done')
    time.sleep(0.5)
    End = time.time()
    print('use: ' + str(End - Start)+'s')
    input('press Enter to exit')
    exit()
