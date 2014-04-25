#-*- coding:utf-8 -*-

from data import get_data
from data import get_commodity_data
import matplotlib.pyplot as plt
import numpy as np

def starcount():
        data = get_data()

        b=[]
        b.append(data[12]['stats_info']['star_info']['1'])
        b.append(data[12]['stats_info']['star_info']['2'])
        b.append(data[12]['stats_info']['star_info']['3'])
        b.append(data[12]['stats_info']['star_info']['4'])
        b.append(data[12]['stats_info']['star_info']['5'])
        
        show(b)
        
def starcount0(asin):
        data = get_commodity_data(asin)

        b = []
        b.append(data['stats_info']['star_info']['1'])
        b.append(data['stats_info']['star_info']['2'])
        b.append(data['stats_info']['star_info']['3'])
        b.append(data['stats_info']['star_info']['4'])
        b.append(data['stats_info']['star_info']['5'])

        show(b)

def show(b):
        x = np.arange(5)
        a = [1,2,3,4,5]

        plt.bar(x, b)
        plt.xticks( x + 0.4,  a)
        plt.xlabel('star')
        plt.ylabel('count')

        plt.show()
