import requests
import json
import jsonpath
from urllib.parse import quote
import random


class Clash_Auto_Proxy:

    headers_clash = {
        'Authorization': 'Bearer b0c43af7-cee4-43b4-97a4-b2158da8b160'
    }

    Order = 0

    def __init__(self, Port, Name) -> None:
        self.url_clash_GetProxies = 'http://127.0.0.1:' + \
            str(Port) + '/providers/proxies'
        self.url_clash_ChangeProxies = 'http://127.0.0.1:' + \
            str(Port) + '/proxies/' + quote(Name)

        response = requests.get(
            url=self.url_clash_GetProxies, headers=self.headers_clash)
        obj = json.loads(response.text)
        self.proxies = jsonpath.jsonpath(
            obj, '$.providers.' + Name + '.proxies..all')[0]
        self.Len = len(self.proxies) - 1

    def Change_Proxy(self, Proxy):
        data_clash_ChangeProxies = {'name': Proxy}
        try:
            response_put = requests.put(
                self.url_clash_ChangeProxies, json=data_clash_ChangeProxies, headers=self.headers_clash)
            return response_put
        except:
            return False

    def Random_Proxy(self):
        Address = random.choice(self.proxies)
        self.Change_Proxy(Address)
        return Address

    def Random_Proxy_With_Order(self, Order_Proxies):
        Address = random.choice(Order_Proxies)
        self.Change_Proxy(Address)
        return Address

    def Order_Proxy(self):
        self.Change_Proxy(self.proxies[self.Order])
        if self.Order == self.Len:
            self.Order = 0
        else:
            self.Order += 1
