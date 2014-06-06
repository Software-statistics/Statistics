#-*- coding:utf-8 -*-

import urllib
import simplejson as json
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
from data import get_category_all
from data import get_category_page

# The number of the star between 1 to 5 of the 100 goods form a sort
# Parameters:category
# Return the number of the star between 1 to 5 of the 100 goods form a sort
def allstar(category):
        data1 = get_category_page(category,1)
        data2 = get_category_page(category,2)
        data3 = get_category_page(category,3)
        data4 = get_category_page(category,4)
        data5 = get_category_page(category,5)
        data=data1+data2+data3+data4+data5
        star_list=[]
        
        a=0
        b=0
        c=0
        d=0
        e=0
        
        for every in data:
                star_list.append(every['stats_info']['avg_info'])
        for each in star_list:
        	if(float(each) <= 1.5 ):
        		a += 1
        	elif(float(each) <= 2.5 ):
        		b += 1
        	elif(float(each) <= 3.5 ):
        		c += 1
        	elif(float(each) <= 4.5 ):
        		d += 1
        	elif(float(each) <= 5 ):
        		e += 1
        result=str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e)
        return result

def highchart(category):
        result = allstar(category)
        a=result.split('/')[0]
        b=result.split('/')[1]
        c=result.split('/')[2]
        d=result.split('/')[3]
        e=result.split('/')[4]

        content='''<script>'''
        content+='''$(function () {'''
        content+='''$('#allstar').highcharts({'''
        content+='''chart: {'''
        content+='''plotBackgroundColor: null,'''
        content+='''plotBorderWidth: null,'''
        content+='''plotShadow: false'''
        content+='''},'''
        content+='''title: {'''
        content+='''text: 'Browser market shares at a specific website, 2010' '''
        content+='''},'''
        content+='''tooltip: {'''
    	content+='''pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>' '''
    	content+='''},'''
        content+='''plotOptions: {'''
        content+='''pie: {'''
        content+='''allowPointSelect: true,'''
        content+='''cursor: 'pointer','''
        content+='''dataLabels: {'''
        content+='''enabled: true,'''
        content+='''color: '#000000','''
        content+='''connectorColor: '#000000','''
        content+='''format: '<b>{point.name}</b>: {point.percentage:.1f} %' '''
        content+='''}'''
        content+='''}'''
        content+='''},'''
        content+='''series: [{'''
        content+='''type: 'pie','''
        content+='''name: 'Browser share','''
        content+='''data: ['''
        content+='''['1',   '''
        content+=a
        content+=''' ],'''
        content+='''['2',   '''
        content+=b
        content+=''' ],'''
        content+='''['3',   '''
        content+=c
        content+=''' ],'''
        content+='''['4',   '''
        content+=d
        content+=''' ],'''
        content+='''['5',   '''
        content+=e
        content+=''' ]'''
        content+=''']'''
        content+='''}]'''
        content+='''});'''
        content+='''});'''
        content+='''</script>'''
        return content
