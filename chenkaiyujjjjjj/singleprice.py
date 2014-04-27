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

        price_list=[]
        date_list=[]
        #print data[0]
        
        for offer in data[5]['offer']:      
                for info in offer['info']:
                        try:
                                date_list.append(datetime.strptime(info['timestamp'], 
                                           '%Y-%m-%d %H:%M:%S'))
                                price_list.append(info['price'])
                        except:
                                pass
        print date_list
        print price_list
        plt.plot(date_list, price_list, 'o-')
        plt.gcf().autofmt_xdate()   #自动调整日期显示的格式
        plt.xlabel('date')
        plt.ylabel('price')
    
        plt.show()
