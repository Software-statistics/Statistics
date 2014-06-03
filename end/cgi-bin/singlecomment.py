#-*- coding:utf-8 -*-

import urllib
import simplejson as json
import matplotlib.pyplot as plt
from datetime import datetime
from data import get_commodity_data

def price(asin):

        data = get_commodity_data(asin)
        publishTime_list=[]

        for every in data['review']:
                publishTime_list.append(every['publishTime'])
                
        publishTimeMonth_list=[0 for i in range(12)]

        for every in publishTime_list:
                if(int(datetime.strptime(every, 
                                           '%Y-%m-%d %H:%M:%S').strftime('%Y'))==2013):
                        publishTimeMonth_list[int(datetime.strptime(every, 
                                           '%Y-%m-%d %H:%M:%S').strftime('%m'))-1]+=1


        mouth= [1,2,3,4,5,6,7,8,9,10,11,12];                      
        str_publishTimeMonth_list = ",".join(str(item) for item in publishTimeMonth_list)
        str_month_list = "','".join(str(item) for item in mouth)
        result=str_month_list+'/'+str_publishTimeMonth_list
        return result

def highchart(asin):
        result = price(asin)
        str_month_list=result.split('/')[0]
        str_publishTimeMonth_list=result.split('/')[1]
        str_asin=asin
#        content='''<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>'''
#        content+='''<script type="text/javascript" src="http://code.highcharts.com/highcharts.js"></script>'''
        content='''<script>'''
        content+='''$(function () {'''
        content+='''$('#comment').highcharts({'''
        content+='''chart: {'''
        content+='''type: 'column' '''
        content+='''},'''
        content+='''title: {'''
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4158a033c3db892395368fd6159b9fc60444b47c
        content+='''text: 'Monthly comment' '''
        content+='''},'''
        content+='''subtitle: { '''
        content+='''text: 'Source: http://trendata.cn' '''
<<<<<<< HEAD
=======
        content+='''text: 'Monthly Average Comment' '''
        content+='''},'''
        content+='''subtitle: { '''
        content+='''text: 'Source: trendata.cn' '''
>>>>>>> FETCH_HEAD
=======
>>>>>>> 4158a033c3db892395368fd6159b9fc60444b47c
        content+='''},'''
        content+='''xAxis: {'''
        content+='''categories: [' '''+str_month_list+''' ']'''
        content+='''},'''
        content+='''yAxis: {'''
        content+='''min: 0,'''
        content+='''title: {'''
        content+='''text:'Price' '''
        content+='''}'''
        content+='''},'''
        content+='''tooltip: {'''
        content+='''headerFormat: '<span style="font-size:10px">{point.key}</span>','''
        content+='''pointFormat: '' +'''
        content+='''   '','''
        content+='''footerFormat: '<table><tbody><tr><td style="color:{series.color};padding:0">{series.name}: </td><td style="padding:0"><b>{point.y:.1f} mm</b></td></tr></tbody></table>','''
        content+='''shared: true,'''
        content+='''useHTML: true'''
        content+='''},'''
        content+='''plotOptions: {'''
        content+='''column: {'''
        content+='''pointPadding: 0.2,'''
        content+='''borderWidth: 0'''
        content+='''}'''
        content+='''},'''
        content+='''series: [{'''
        content+='''name:' '''+str_asin+"',"
        content+='''data: ['''+str_publishTimeMonth_list+''' ]'''
        content+='''}]'''
        content+='''});'''
        content+='''});'''
        content+='''</script>'''
        return content
