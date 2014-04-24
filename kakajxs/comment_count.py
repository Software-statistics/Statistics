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
        review_list=[]


        for goods in data:
                comment_count_list.append(goods['stats_info']['review_count'])
                goods_list.append(goods['ASIN'])
                review_list.append(goods['review'])

        publishTime_list=[]

        for every in review_list[12]:
                publishTime_list.append(every['publishTime'])
        print datetime.strptime(publishTime_list[0], 
                                           '%Y-%m-%d %H:%M:%S').strftime('%Y-%m')

        publishTimeMonth_list=[0 for i in range(12)]

        for every in publishTime_list:
                if(int(datetime.strptime(every, 
                                           '%Y-%m-%d %H:%M:%S').strftime('%Y'))==2013):
                        publishTimeMonth_list[int(datetime.strptime(every, 
                                           '%Y-%m-%d %H:%M:%S').strftime('%m'))-1]+=1

        print publishTimeMonth_list
        
        #print goods_list
        #print comment_count_list

        #print len(goods_list)
        #print len(comment_count_list)

##        x = np.arange(len(goods_list))
##
##
##        formatter = FuncFormatter(millions)
##
##        fig, ax = plt.subplots()
##        ax.yaxis.set_major_formatter(formatter)
##        plt.bar(x, comment_count_list)
##        plt.xticks( x + 0.5,  goods_list)

        plt.plot([1,2,3,4,5,6,7,8,9,10,11,12], publishTimeMonth_list, 'o--')
        plt.gcf().autofmt_xdate()   #自动调整日期显示的格式
        plt.xlabel('month')
        plt.ylabel('number')
    
        plt.show()

