#-*- coding:utf-8 -*-

import urllib
import simplejson as json
import matplotlib.pyplot as plt
from datetime import datetime

REQUEST_URL = 'http://112.124.1.3:8004'


def show_something():

        target_url='http://112.124.1.3:8004/api/commodity?category_name=Shoes>Boys>Outdoor&page=2'

        data = json.loads(urllib.urlopen(target_url).read())
        return data


if __name__ == '__main__':
        data = show_something()
        price_list = []
        avg_price=[]

        for single in data:
            for offer in single['offer']:
                for info in offer['info']:
                    try:
                        price_list.append(info['price'])
                    except:
                        pass
            avg_price.append(price_list.pop())
        #for single in avg_price:
                
        print avg_price
