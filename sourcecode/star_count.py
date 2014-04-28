#-*- coding:utf-8 -*-

from data import get_category_data
from data import get_category_all
from data import get_commodity_data
from data import get_category_count
import matplotlib.pyplot as plt
import numpy as np

# sortn
def starcount(sort, n):
        data = get_category_data(sort,n)

        b=[]
        b.append(data[n]['stats_info']['star_info']['1'])
        b.append(data[n]['stats_info']['star_info']['2'])
        b.append(data[n]['stats_info']['star_info']['3'])
        b.append(data[n]['stats_info']['star_info']['4'])
        b.append(data[n]['stats_info']['star_info']['5'])
        
        show(b)
   
# asin     
def starcount0(asin):
        data = get_commodity_data(asin)

        b = []
        b.append(data['stats_info']['star_info']['1'])
        b.append(data['stats_info']['star_info']['2'])
        b.append(data['stats_info']['star_info']['3'])
        b.append(data['stats_info']['star_info']['4'])
        b.append(data['stats_info']['star_info']['5'])

        show(b)

# sort
def starcountall(sort):
        data = get_category_all(sort)
        
        star_count_list=[]
        
        a=0
        b=0
        c=0
        d=0
        e=0
        
        for single in data:
        	for i in range(0,19):
        		try:
        			star_count_list.append(single[i]['stats_info']['avg_info'])
        		except:
        			pass

        for each in star_count_list:
        	if(float(each) <= 1 ):
        		a += 1
        	elif(float(each) <= 2 ):
        		b += 1
        	elif(float(each) <= 3 ):
        		c += 1
        	elif(float(each) <= 4 ):
        		d += 1
        	elif(float(each) <= 5 ):
        		e += 1
        
        labels = ['1', '2', '3', '4','5']
        sizes = [a, b, c, d, e]
        colors = ['gold' , 'black','yellowgreen', 'lightcoral','lightskyblue']
        explode = (0, 0, 0, 0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')
        
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=False)
        
        # Set aspect ratio to be equal so that pie is drawn as a circle.
        
        plt.title('')
        plt.axis('equal')
        plt.show()

# 
def show(b):
        x = np.arange(5)
        a = [1,2,3,4,5]

        plt.bar(x, b,color = 'red')
        plt.xticks( x + 0.4,  a)
        plt.xlabel('star')
        plt.ylabel('count')

        plt.show()
