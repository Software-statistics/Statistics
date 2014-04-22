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


if __name__ == '__main__':
        data = show_something()

        comment_count_list=[]
        goods_list=[]
        

        for goods in data:
                comment_count_list.append(goods['stats_info']['review_count'])
                goods_list.append(goods['ASIN'])
        	

        print goods_list
        print comment_count_list

        print len(goods_list)
        print len(comment_count_list)

        x = np.arange(len(goods_list))


        formatter = FuncFormatter(millions)

        fig, ax = plt.subplots()
        ax.yaxis.set_major_formatter(formatter)
        plt.bar(x, comment_count_list)
        plt.xticks( x + 0.5,  goods_list)

    
        plt.show()

