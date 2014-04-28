#-*- coding:utf-8 -*-

import urllib
from datetime import datetime
import simplejson as json
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np

REQUEST_URL = 'http://112.124.1.3:8004'


def show_something():
        all_c = 'api/commodity/'
        sort = 'Shoes>Boys>Outdoor'
        data = json.loads(urllib.urlopen('?'.join([('/'.join([REQUEST_URL,all_c])),urllib.urlencode({'category_name':sort,'page':1})])).read())
        #data2 = json.loads(urllib.urlopen('?'.join([('/'.join([REQUEST_URL,all_c])),urllib.urlencode({'category_name':sort,'page':2})])).read())
        #data3 = json.loads(urllib.urlopen('?'.join([('/'.join([REQUEST_URL,all_c])),urllib.urlencode({'category_name':sort,'page':3})])).read())
        #data4 = json.loads(urllib.urlopen('?'.join([('/'.join([REQUEST_URL,all_c])),urllib.urlencode({'category_name':sort,'page':4})])).read())
        #data=data1+data2+data3+data4
        return data

if __name__ == '__main__':
        data = show_something()
        comment_count_list=[]
        star_list=[]
        goods_list=[]
        
        for goods in data:
                comment_count_list.append(goods['stats_info']['review_count'])
                star_list.append(float(goods['stats_info']['avg_info'])/0.01-200)
                goods_list.append(goods['ASIN'])
        print star_list
        
        plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], comment_count_list, 'o--')
        plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], star_list, 'o--')
        plt.gcf().autofmt_xdate()   #自动调整日期显示的格式
        plt.xlabel('ASIN')
        plt.ylabel('number')
        plt.show()
