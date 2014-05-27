#-*- coding:utf-8 -*-

import urllib
import simplejson as json
import matplotlib.pyplot as plt
from datetime import datetime
from data import get_commodity_data

def price(asin):

        data = get_commodity_data(asin)
        price_list=[]
        date_list=[]
        print data
        
        for offer in data['offer']:      
                for info in offer['info']:
                        try:
                                date_list.append(datetime.strptime(info['timestamp'], 
                                           '%Y-%m-%d %H:%M:%S'))
                                price_list.append(info['price'])
                        except:
                                pass
        show(price_list,date_list)

def show(price_list,date_list):
        
        plt.plot(date_list, price_list, 'o-')
        plt.gcf().autofmt_xdate()   #自动调整日期显示的格式
        plt.xlabel('date')
        plt.ylabel('price')
    
        plt.show()
