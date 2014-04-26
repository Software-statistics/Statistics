#-*- coding:utf-8 -*-

import urllib
import simplejson as json
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

REQUEST_URL = 'http://112.124.1.3:8004'

def show_something():

        target_url1='http://112.124.1.3:8004/api/commodity?category_name=Shoes>Boys>Outdoor&page=1'
        target_url2='http://112.124.1.3:8004/api/commodity?category_name=Shoes>Boys>Outdoor&page=2'
        target_url3='http://112.124.1.3:8004/api/commodity?category_name=Shoes>Boys>Outdoor&page=3'
        target_url4='http://112.124.1.3:8004/api/commodity?category_name=Shoes>Boys>Outdoor&page=4'
        data1 = json.loads(urllib.urlopen(target_url1).read())
        data2 = json.loads(urllib.urlopen(target_url2).read())
        data3 = json.loads(urllib.urlopen(target_url3).read())
        data4 = json.loads(urllib.urlopen(target_url4).read())
        data = data1+data2+data3+data4
        return data

if __name__ == '__main__':
        data = show_something()
        price_list = []
        avg_price=[]
        price_range=[0 for i in range(6)]

        for single in data:
            for offer in single['offer']:
                for info in offer['info']:
                    try:
                        price_list.append(info['price'])
                    except:
                        pass
            avg_price.append(price_list.pop())
        for single in avg_price:
                if single<20:
                        price_range[0] = price_range[0]+1
                elif single<40 and single>=20:
                        price_range[1] = price_range[1]+1
                elif single<60 and single>=40:
                        price_range[2] = price_range[2]+1
                elif single<80 and single>=60:
                        price_range[3] = price_range[3]+1
                elif single<100 and single>=80:
                        price_range[4] = price_range[4]+1
                else:
                        price_range[5] = price_range[5]+1
        print avg_price
        print price_range
        
        plt.hist(avg_price,6,color='red')
        plt.xlabel('price')
        plt.ylabel('count')
        plt.show()
