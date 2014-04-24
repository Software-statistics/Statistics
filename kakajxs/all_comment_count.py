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

        data = json.loads(urllib.urlopen('?'.join([('/'.join([REQUEST_URL,all_c])),urllib.urlencode({'category_name':sort})])).read())
        return data

if __name__ == '__main__':
        data = show_something()
        comment_count_list=[]
        goods_list=[]
        kind_list=[0 for i in range(11)]
        
        for goods in data:
                comment_count_list.append(goods['stats_info']['review_count'])
                goods_list.append(goods['ASIN'])
        plt.hist(comment_count_list, color ='grey', align = 'mid', bins = 5, rwidth = 0.5)
        plt.show()

