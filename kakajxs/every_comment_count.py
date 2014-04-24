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
        review_list=[]


        for goods in data:
                review_list.append(goods['review'])

        publishTime_list=[]

        for every in review_list[12]:
                publishTime_list.append(every['publishTime'])
        

        publishTimeMonth_list=[0 for i in range(12)]

        for every in publishTime_list:
                if(int(datetime.strptime(every, 
                                           '%Y-%m-%d %H:%M:%S').strftime('%Y'))==2013):
                        publishTimeMonth_list[int(datetime.strptime(every, 
                                           '%Y-%m-%d %H:%M:%S').strftime('%m'))-1]+=1


        plt.plot([1,2,3,4,5,6,7,8,9,10,11,12], publishTimeMonth_list, 'o--')
        plt.gcf().autofmt_xdate()   #自动调整日期显示的格式
        plt.xlabel('month')
        plt.ylabel('number')
    
        plt.show()

