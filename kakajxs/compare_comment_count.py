#-*- coding:utf-8 -*-

import urllib
from datetime import datetime
import simplejson as json
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np

REQUEST_URL = 'http://112.124.1.3:8004'


def show_something1():

        all_c = 'api/commodity/'
        sort = 'Beauty>Bath & Body>Bath'

        data = json.loads(urllib.urlopen('?'.join([('/'.join([REQUEST_URL,all_c])),urllib.urlencode({'category_name':sort})])).read())
        return data

def show_something2():

        all_c = 'api/commodity/'
        sort = 'Beauty>Bath & Body>Bathing Accessories'

        data = json.loads(urllib.urlopen('?'.join([('/'.join([REQUEST_URL,all_c])),urllib.urlencode({'category_name':sort})])).read())
        return data

if __name__ == '__main__':
        data1 = show_something1()
        data2 = show_something2()
        review_list1=[]
        review_list2=[]


        for goods in data1:
                review_list1.append(goods['review'])

        for goods in data2:
                review_list2.append(goods['review'])

        publishTime_list1=[]
        publishTime_list2=[]

        for each in review_list1:
                for every in each:
                        publishTime_list1.append(every['publishTime'])

        for each in review_list2:
                for every in each:
                        publishTime_list2.append(every['publishTime'])
        

        publishTimeMonth_list1=[0 for i in range(12)]
        publishTimeMonth_list2=[0 for i in range(12)]

        
        for every in publishTime_list1:
                if(int(datetime.strptime(every, 
                                           '%Y-%m-%d %H:%M:%S').strftime('%Y'))==2013):
                        publishTimeMonth_list1[int(datetime.strptime(every, 
                                           '%Y-%m-%d %H:%M:%S').strftime('%m'))-1]+=1

        for every in publishTime_list2:
                if(int(datetime.strptime(every, 
                                           '%Y-%m-%d %H:%M:%S').strftime('%Y'))==2013):
                        publishTimeMonth_list2[int(datetime.strptime(every, 
                                           '%Y-%m-%d %H:%M:%S').strftime('%m'))-1]+=1

        plt.plot([1,2,3,4,5,6,7,8,9,10,11,12], publishTimeMonth_list1, 'o--')
        plt.plot([1,2,3,4,5,6,7,8,9,10,11,12], publishTimeMonth_list2, 'o--')
        plt.gcf().autofmt_xdate()   #自动调整日期显示的格式
        plt.xlabel('month')
        plt.ylabel('number')
    
        plt.show()

