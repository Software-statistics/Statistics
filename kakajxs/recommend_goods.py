#-*- coding:utf-8 -*-

import urllib
import simplejson as json
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
from data import get_category_all
from data import get_category_page

def recommendcommodity(category):
        data1 = get_category_page(category,1)
        data=data1
        ASIN_list=[0 for i in range(4)]
        compare_list=[0 for i in range(4)]

        record=0;
        ASIN_list[0]=data[0]['ASIN']
        compare_list[0]=float(data[0]['stats_info']['review_count'])+float(data[0]['stats_info']['avg_info'])*10
        number = len(data)
        for i in range(0,number):
                if((float(data[i]['stats_info']['review_count'])+float(data[i]['stats_info']['avg_info'])*10)>compare_list[0]):
                        ASIN_list[0]=data[i]['ASIN']
                        compare_list[0]=float(data[i]['stats_info']['review_count'])+float(data[i]['stats_info']['avg_info'])*10
                        record=i
        data.remove(data[record])
        
        ASIN_list[1]=data[0]['ASIN']
        compare_list[1]=float(data[0]['stats_info']['review_count'])+float(data[0]['stats_info']['avg_info'])*10
        number = len(data)
        for i in range(0,number):
                if((float(data[i]['stats_info']['review_count'])+float(data[i]['stats_info']['avg_info'])*10)>compare_list[1]):
                        ASIN_list[1]=data[i]['ASIN']
                        compare_list[1]=float(data[i]['stats_info']['review_count'])+float(data[i]['stats_info']['avg_info'])*10
                        record=i
        data.remove(data[record])

        ASIN_list[2]=data[0]['ASIN']
        compare_list[2]=float(data[0]['stats_info']['review_count'])+float(data[0]['stats_info']['avg_info'])*10
        number = len(data)
        for i in range(0,number):
                if((float(data[i]['stats_info']['review_count'])+float(data[i]['stats_info']['avg_info'])*10)>compare_list[2]):
                        ASIN_list[2]=data[i]['ASIN']
                        compare_list[2]=float(data[i]['stats_info']['review_count'])+float(data[i]['stats_info']['avg_info'])*10
                        record=i
        data.remove(data[record])

        ASIN_list[3]=data[0]['ASIN']
        compare_list[3]=float(data[0]['stats_info']['review_count'])+float(data[0]['stats_info']['avg_info'])*10
        number = len(data)
        for i in range(0,number):
                if((float(data[i]['stats_info']['review_count'])+float(data[i]['stats_info']['avg_info'])*10)>compare_list[3]):
                        ASIN_list[3]=data[i]['ASIN']
                        compare_list[3]=float(data[i]['stats_info']['review_count'])+float(data[i]['stats_info']['avg_info'])*10
                        record=i
        data.remove(data[record])
        return ASIN_list
	
def recommendprice(asin):
	return price

if __name__ == '__main__':
        category='Shoes>Boys>Outdoor'
        ASIN_list=recommendcommodity(category)
        print ASIN_list
