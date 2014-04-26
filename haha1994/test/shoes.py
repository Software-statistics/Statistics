#-*- coding:utf-8 -*-

import urllib
import simplejson as json
import matplotlib.pyplot as plt
from datetime import datetime
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

REQUEST_URL = 'http://112.124.1.3:8004'


def show_something():

        all_c = 'api/commodity/'
        sort = 'Shoes>Boys>Outdoor'

#        ,'field':['ASIN']

 
        

        data = json.loads(urllib.urlopen('?'.join([('/'.join([REQUEST_URL,all_c])),urllib.urlencode({'category_name':sort})])).read())
#        for single in data:
#                print single['ASIN']
        return data


if __name__ == '__main__':
        data = show_something()

        price_list=[]
        date_list=[]

        
        for offer in data[0]['offer']:
                try:
                        date_list.append(datetime.strptime(offer['info'][0]['timestamp'], 
                                           '%Y-%m-%d %H:%M:%S'))
                        price_list.append(offer['info'][0]['price'])
  
                except:
                        print 'out of range'

        plt.plot(date_list, price_list, 'o--')
        plt.gcf().autofmt_xdate()   #自动调整日期显示的格式
        plt.xlabel('date')
        plt.ylabel('price')
    
        plt.show()
        
