# Pixiv_Download

一个用于批量下载一个Pixiv作者的所有作品的python程序

**起因**是近期发生的一件令人唏嘘的事——两位优秀的画师因发布**有关游戏解包内容的画作**被某些群体**疯狂网暴、开盒**以至于**删除所有作品并毁号**无奈退入幕后，在舆论上帮助这两位画师的同时，我也深感**保留喜爱作者的所有作品**的重要性，正好这几天又在《尚硅谷》的爬虫系列课程中学习，于是便以此作为**阶段性**的**学习成果验证**

这是一个**作业**类型的项目，实用性和美观程度**远不如**同类型的上千star的项目，如果你**只是想使用**的话，建议去使用那些项目，如果你和我一样只是一个**初学者**，那我希望这个项目能给你些许的帮助

## 使用方法
获取所有文件后运行main.py

第一次运行会生成一个Settings.json文件，你需要在这个文件内设置你需要的选项

而后再次运行

## 实现方法特点(不足)
自动切换代理的方法并不是常规的设置国外代理池，而是利用廉价的科学上网平台进行代理

即抓取ClashForWindows的网页控制Api，而后使用Api控制代理节点的切换

## 库
requests，
json,
jsonpath,
urllib.parse.quote,
random,
time,
os,
lxml.etree
