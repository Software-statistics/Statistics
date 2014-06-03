# -*- coding:utf-8 -*-

import urllib
import simplejson as json
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
from data import get_category_page

#求一个商品分类中商品的排名和评论数之间的关系
#传入商品分类和需获取数据的页数
#返回按照排名排好序的商品的评论数
def rankandcomment(sort,page):
    data=[]
    comment_count_list=[]
    rank_list=[]
    all_list=[]
    str_rank_list1=[]
    str_rank_list2=[]
    new_comment_count_list=[]
    last_comment_count_list=[]
    alist=[]
    new_dict={}
    for i in range(1,page+1):
        single=get_category_page(sort,i)
        data=data+single
    for single in data:
        for productInfo in single['productInfo']:
            for productDetail in productInfo['productDetail']:
                try:
                    rank_list.append(productDetail['bestSellerRank'][0])
                except:
                    pass
        comment_count_list.append(single['stats_info']['review_count'])
        num=len(rank_list)
    #print len(rank_list)
    #print num
    for i in range(0,num):
        al=str(rank_list[i])+';'+str(comment_count_list[i])
        all_list.append(al)
    #print all_list
    for single in all_list:
        str_rank1=single.split('[')[0]
        str_rank2=str_rank1.split('#')[1]
        str_rank3=single.split('[')[1]
        str_rank4=str_rank3.split(';')[1]
        str_rank_list2.append(str_rank4)
        str_rank2=str_rank2.replace(',','')
        m=int(str_rank2)
        #print m
        str_rank_list1.append(m)
    #print str_rank_list1
    #print str_rank_list2
    new_dict=dict(zip(str_rank_list1,str_rank_list2))
    new_dict=sorted(new_dict.iteritems(),key=lambda x:x[0])
    for single in new_dict:
        ss=single[1]
        n=int(ss)
        last_comment_count_list.append(n)
    alist=last_comment_count_list[0:20]
    rank=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    str_alist=','.join(str(item) for item in alist)
    str_rank= "','".join(str(item) for item in rank)
    result = str_alist+'/'+str_rank
    return result
    #print alist
    
def highchart(sort,page):
    result = rankandcomment(sort,page)
    str_alist=result.split('/')[0]
    str_rank=result.split('/')[1]
    str_sort=sort
    content='''<script>'''
    content+='''$(function () {'''
    content+='''$('#rankandcomment').highcharts({chart: {type: 'column',},title: {text:'RankAndComment' },'''
    content+=''' xAxis: {title:{text:'Rank'},categories: [' '''+str_rank+''' ']},'''
    content+='''yAxis: {title: {text:'Comment'}},'''
    content+='''legend: {enabled: false},'''
    content+='''series: [{name:' '''+str_sort+''' ',data:['''_str_alist+'''],dataLabels: {enabled: true,rotation: -90,color: '#FFFFFF',align: 'right',x: 4,y: 10,'''
    content+='''style: {fontSize: '13px',fontFamily: 'Verdana, sans-serif',textShadow: '0 0 3px black}}}]});});'''
    content+='''</script>'''
    return content
