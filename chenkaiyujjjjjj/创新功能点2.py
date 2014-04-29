# -*- coding:utf-8 -*-

import urllib
import simplejson as json
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np


def show_something():
    target_url1='http://112.124.1.3:8004/api/commodity?category_name=Shoes>Boys>Outdoor&page=1'
    target_url2='http://112.124.1.3:8004/api/commodity?category_name=Shoes>Boys>Outdoor&page=2'
    target_url3='http://112.124.1.3:8004/api/commodity?category_name=Shoes>Boys>Outdoor&page=3'
    target_url4='http://112.124.1.3:8004/api/commodity?category_name=Shoes>Boys>Outdoor&page=4'
    data1 = json.loads(urllib.urlopen(target_url1).read())
    data2 = json.loads(urllib.urlopen(target_url2).read())
    data3 = json.loads(urllib.urlopen(target_url3).read())
    data4 = json.loads(urllib.urlopen(target_url4).read())
    data = data1+data2+data3+data4
    return data

if __name__ == '__main__':
    data = show_something()
    comment_count_list=[]
    rank_list=[]
    all_list=[]
    str_rank_list1=[]
    str_rank_list2=[]
    new_comment_count_list=[]
    last_comment_count_list=[]
    new_dict={}

    for single in data:
        for productInfo in single['productInfo']:
            for productDetail in productInfo['productDetail']:
                try:
                    rank_list.append(productDetail['bestSellerRank'][1])
                except:
                    pass
        comment_count_list.append(single['stats_info']['review_count'])
    for i in range(0,19):
        al=str(rank_list[i])+';'+str(comment_count_list[i])
        all_list.append(al)
    for single in all_list:
        str_rank1=single.split('[')[0]
        str_rank2=str_rank1.split('#')[1]
        str_rank3=single.split('[')[1]
        str_rank4=str_rank3.split(';')[1]
        str_rank_list2.append(str_rank4)
        m=int(str_rank2)
        #print m
        str_rank_list1.append(m)
    new_dict=dict(zip(str_rank_list2,str_rank_list1))
    new_dict=sorted(new_dict.iteritems(),key=lambda x:x[1])
    for single in new_dict:
        ss=single[0]
        n=int(ss)
        last_comment_count_list.append(n)

    plt.xlabel('rank')
    plt.ylabel('comment')
    plt.bar(left=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18),height=last_comment_count_list,width=0.5,align="center")
    #plt.hist(last_comment_count_list1,bins=18,color='red')
    plt.show()
    print last_comment_count_list
    print new_dict
