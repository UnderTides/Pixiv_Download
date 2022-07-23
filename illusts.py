import json
import jsonpath
import requests
import proxy
from lxml import etree
import os


class Pixiv_illusts:
    ProxySwitch = False

    illusts = {}
    urls = {}

    headers_Without_Cookie = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    headers_With_Referer = {
        'referer': 'https://www.pixiv.net/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    def __init__(self, cookie) -> None:
        self.headers_With_Cookie = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'cookie': cookie
        }

    def Get_Proxies(self, Port, Name):
        self.Proxy = proxy.Clash_Auto_Proxy(Port, Name)
        print('Got Proxies :')
        print(self.Proxy.proxies)
        self.ProxySwitch = True

    def Get_illusts(self, Author):
        url_Pixiv_Author = 'https://www.pixiv.net/ajax/user/' + \
            str(Author) + '/profile/all'
        response = requests.get(url=url_Pixiv_Author,
                                headers=self.headers_With_Cookie)
        obj = json.loads(response.text)
        self.illusts.update(jsonpath.jsonpath(obj, '$..illusts')[0])

    def Get_urls(self, Timeout=2):
        Total = len(self.illusts)
        Now = 0

        for j in self.illusts:
            illusts_url = 'https://www.pixiv.net/artworks/' + j
            success = True
            while success:
                try:
                    response = requests.get(
                        url=illusts_url, headers=self.headers_Without_Cookie, timeout=Timeout)
                    success = False
                except:
                    print('Timeout! retrying...')
                    success = True
            html_tree = etree.HTML(response.text)
            result = html_tree.xpath(
                '//meta[@id="meta-preload-data"]/@content')[0]
            obj = json.loads(result)
            PageCount = jsonpath.jsonpath(obj, 'illust.'+j+'.pageCount')[0]
            url_result = jsonpath.jsonpath(obj, '$..original')[0]
            for p in range(PageCount):
                self.urls[url_result.replace('p0', 'p'+str(p))] = j+'_p'+str(p)
            Now += 1
            print('Total:'+str(Total)+' Now:'+str(Now) +
                  ' ID:'+str(j)+' Page:'+str(PageCount))

    def Get_urls_With_Proxy(self, Batch, Timeout=2):
        if not self.ProxySwitch:
            return 'No Proxy！ Please use Get_urls()'

        Total = len(self.illusts)
        Now = 0
        i = 0

        for j in self.illusts:
            illusts_url = 'https://www.pixiv.net/artworks/' + j
            success = True
            while success:
                try:
                    response = requests.get(
                        url=illusts_url, headers=self.headers_Without_Cookie, timeout=Timeout
                    )
                    success = False
                except:
                    print('Timeout! retrying...')
                    success = True
            html_tree = etree.HTML(response.text)
            result = html_tree.xpath(
                '//meta[@id="meta-preload-data"]/@content')[0]
            obj = json.loads(result)
            PageCount = jsonpath.jsonpath(obj, 'illust.'+j+'.pageCount')[0]
            url_result = jsonpath.jsonpath(obj, '$..original')[0]
            for p in range(PageCount):
                self.urls[url_result.replace('p0', 'p'+str(p))] = j+'_p'+str(p)
            Now += 1
            print('Total:'+str(Total)+' Now:'+str(Now) +
                  ' ID:'+str(j)+' Page:'+str(PageCount))
            i += 1
            if i >= Batch:
                print(self.Proxy.Random_Proxy())
                i = 0

    def Get_urls_With_Proxy_Order(self, Batch, Order, Timeout=2):
        if not self.ProxySwitch:
            return 'No Proxy！ Please use Get_urls()'

        Total = len(self.illusts)
        Now = 0
        i = 0

        for j in self.illusts:
            illusts_url = 'https://www.pixiv.net/artworks/' + j
            success = True
            while success:
                try:
                    response = requests.get(
                        url=illusts_url, headers=self.headers_Without_Cookie, timeout=Timeout)
                    success = False
                except:
                    print('Timeout! retrying...')
                    success = True
            html_tree = etree.HTML(response.text)
            result = html_tree.xpath(
                '//meta[@id="meta-preload-data"]/@content')[0]
            obj = json.loads(result)
            PageCount = jsonpath.jsonpath(obj, 'illust.'+j+'.pageCount')[0]
            url_result = jsonpath.jsonpath(obj, '$..original')[0]
            for p in range(PageCount):
                self.urls[url_result.replace('p0', 'p'+str(p))] = j+'_p'+str(p)
            Now += 1
            print('Total:'+str(Total)+' Now:'+str(Now) +
                  ' ID:'+str(j)+' Page:'+str(PageCount))
            i += 1
            if i >= Batch:
                print(self.Proxy.Random_Proxy_With_Order(Order))
                i = 0

    def Get_artworks(self, Timeout=10):
        Total = len(self.urls)
        Now = 0
        path = './img'

        if not os.path.exists(path):
            os.mkdir(path)

        for j in self.urls:
            success = True
            while success:
                try:
                    img = requests.get(
                        j, headers=self.headers_With_Referer, timeout=Timeout)
                    success = False
                except:
                    print('Timeout! retrying...')
                    success = True
            ID = str(self.urls[j])
            with open('./img/' + ID + j.split('.')[-1], 'wb') as im:
                im.write(img.content)
            Now += 1
            print('Total:'+str(Total)+' Now:'+str(Now)+' ID:'+ID)

    def Get_artworks_With_Proxy(self, Batch, Timeout=10):
        if not self.ProxySwitch:
            return 'No Proxy！ Please use Get_artworks()'

        Total = len(self.urls)
        Now = 0
        i = 0
        path = './img'

        if not os.path.exists(path):
            os.mkdir(path)

        for j in self.urls:
            success = True
            while success:
                try:
                    img = requests.get(
                        j, headers=self.headers_With_Referer, timeout=Timeout)
                    success = False
                except:
                    print('Timeout! retrying...')
                    success = True
            ID = str(self.urls[j])
            with open('./img/' + ID + j.split('.')[-1], 'wb') as im:
                im.write(img.content)
            Now += 1
            print('Total:'+str(Total)+' Now:'+str(Now)+' ID:'+ID)
            i += 1
            if i >= Batch:
                print(self.Proxy.Random_Proxy())
                i = 0

    def Get_artworks_With_Proxy_Order(self, Batch, Order, Timeout=10):
        if not self.ProxySwitch:
            return 'No Proxy！ Please use Get_artworks()'

        Total = len(self.urls)
        Now = 0
        i = 0
        path_base = './img'
        path = './img'
        p = 1

        while os.path.exists(path):
            path = path_base+str(p)
            p += 1
        os.mkdir(path)

        for j in self.urls:
            success = True
            while success:
                try:
                    img = requests.get(
                        j, headers=self.headers_With_Referer, timeout=Timeout)
                    success = False
                except:
                    print('Timeout! retrying...')
                    success = True
            ID = str(self.urls[j])
            with open(path + './'+ID + '.' + j.split('.')[-1], 'wb') as im:
                im.write(img.content)
            Now += 1
            print('Total:'+str(Total)+' Now:'+str(Now)+' ID:'+ID)
            i += 1
            if i >= Batch:
                print(self.Proxy.Random_Proxy_With_Order(Order))
                i = 0
