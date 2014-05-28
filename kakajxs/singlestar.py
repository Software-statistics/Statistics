#-*- coding:utf-8 -*-

import urllib
import simplejson as json
import matplotlib.pyplot as plt
from datetime import datetime
from data import get_commodity_data

def price(asin):

        data = get_commodity_data(asin)
        publishTime_list=[]
        star_list=[]
        for every in data['review']:
                publishTime_list.append(every['publishTime'])
        for every in data['review']:
                star_list.append(every['star'])

        publishTimeMonth_list=[0 for i in range(12)]        
        starMonth_list=[0 for i in range(12)]
        number = len(publishTime_list)
        for i in range(0,number):
                if(int(datetime.strptime(publishTime_list[i], 
                                           '%Y-%m-%d %H:%M:%S').strftime('%Y'))==2013):
                        starMonth_list[int(datetime.strptime(publishTime_list[i], 
                                           '%Y-%m-%d %H:%M:%S').strftime('%m'))-1]+=float(star_list[i].split(' ')[0])
                        publishTimeMonth_list[int(datetime.strptime(publishTime_list[i], 
                                           '%Y-%m-%d %H:%M:%S').strftime('%m'))-1]+=1
        for i in range(0,len(starMonth_list)):
                starMonth_list[i-1]=starMonth_list[i-1]/publishTimeMonth_list[i-1]


        mouth= [1,2,3,4,5,6,7,8,9,10,11,12];                      
        str_starMonth_list = ",".join(str(item) for item in starMonth_list)
        str_month_list = "','".join(str(item) for item in mouth)
        result=str_month_list+'/'+str_starMonth_list
        return result

def highchart(asin):
        result = price(asin)
        str_month_list=result.split('/')[0]
        str_starMonth_list=result.split('/')[1]
        str_asin=asin
        content='''<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>'''
        content+='''<script type="text/javascript" src="http://code.highcharts.com/highcharts.js"></script>'''
        content+='''<script>'''
        content+='''$(function () {'''
        content+='''$('#container').highcharts({'''
        content+='''title: {'''
        content+='''text: 'Price Trend','''
        content+='''x: -20'''
        content+='''},'''
        content+='''xAxis: {'''
        content+='''title:{'''
        content+='''text:'Date' '''
        content+='''},'''
        content+='''categories: [' '''+str_month_list+''' ']'''
        content+='''},'''
        content+='''yAxis: {'''
        content+='''title: {'''
        content+='''text:'Price' '''
        content+='''},'''
        content+='''},'''
        content+='''legend: {'''
        content+='''layout: 'vertical','''
        content+='''align: 'right','''
        content+='''verticalAlign: 'middle','''
        content+='''borderWidth: 0'''
        content+='''},'''
        content+='''series: [{'''
        content+='''name:' '''+str_asin+"',"
        content+='''data: ['''+str_starMonth_list+''' ]'''
        content+='''}]'''
        content+='''});'''
        content+='''});'''
        content+='''</script>'''
        content+='''<div id="container" style="min-width: 310px; height: 400px; margin: 0 auto"></div>'''
        return content
