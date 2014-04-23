#-*- coding:utf-8 -*-

import urllib
import simplejson as json
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np

REQUEST_URL = 'http://112.124.1.3:8004'


def show_something():

        all_c = 'api/commodity/'
        sort = 'Shoes>Boys>Outdoor'

        data = json.loads(urllib.urlopen('?'.join([('/'.join([REQUEST_URL,all_c])),urllib.urlencode({'category_name':sort})])).read())
#        for single in data:
#                print single['ASIN']
        return data

def millions(x, pos):
    'The two args are the value and tick position'
    return '%1.1f' % (x)

def analyse(a):
        m = a['1'] + 2.0 * a['2'] + 3.0 * a['3'] + 4.0 * a['4'] + 5.0 * a['5']
        n = a['1'] + a['2'] + a['3'] + a['4'] + a['5']
        if(n==0):
            return 0
        return m/n


if __name__ == '__main__':
        data = show_something()

        star_count_list=[]
        goods_list=[]
        

        for goods in data:
                star_count_list.append(analyse(goods['stats_info']['star_info']))
                goods_list.append(goods['ASIN'])
        	
<<<<<<< HEAD
=======

>>>>>>> FETCH_HEAD
        print goods_list
        print star_count_list

        print len(goods_list)
        print len(star_count_list)
<<<<<<< HEAD
=======

>>>>>>> FETCH_HEAD

        x = np.arange(len(goods_list))


        formatter = FuncFormatter(millions)

        fig, ax = plt.subplots()
        ax.yaxis.set_major_formatter(formatter)
        plt.bar(x, star_count_list)
        plt.xticks( x + 0.5,  goods_list)

    
        plt.show()

