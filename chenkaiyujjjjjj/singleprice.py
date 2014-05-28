#-*- coding:utf-8 -*-

import urllib
import simplejson as json
import matplotlib.pyplot as plt
from datetime import datetime
from data import get_commodity_data

def price(asin):

        data = get_commodity_data(asin)
        price_list=[]
        date_list=[]
        average_price=[]
        average_date=[]
        #print data
        
        for offer in data['offer']:      
                for info in offer['info']:
                        try:
                                date_list.append(datetime.strptime(info['timestamp'], 
                                           '%Y-%m-%d %H:%M:%S'))
                                price_list.append(info['price'])
                        except:
                                pass
        #print price_list
        number = len(date_list)
        #print number
        for i in range(0,number):
                n=1
                sum_price=float(price_list[i])
                for j in range(i+1,number):
                        if date_list[i]==date_list[j]:
                                sum_price=sum_price+float(price_list[j])
                                n=n+1
                                del price_list[j]
                                price_list.insert(j,0)
                                del date_list[j]
                                date_list.insert(j,'')
                if int(sum_price/n)!=0 and date_list[i]!='':
                        average_price.append('%.2f' %(sum_price/n))
                        average_date.append(date_list[i])
        str_date = "','".join(str(item) for item in average_date)
        str_price=','.join(str(item) for item in average_price)
        result=str_date+'/'+str_price
        return result

def highchart(asin):
        result = price(asin)
        str_date=result.split('/')[0]
        str_price=result.split('/')[1]
        str_asin=asin
        #print str_date
        #print str_price
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
        content+='''categories: [' '''+str_date+''' ']'''
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
        content+='''data: ['''+str_price+''']'''
        content+='''}]'''
        content+='''});'''
        content+='''});'''
        content+='''</script>'''
        content+='''<div id="container" style="min-width: 310px; height: 400px; margin: 0 auto"></div>'''
        return content

def show(price_list,date_list):
        
        plt.plot(date_list, price_list, 'o-')
        plt.gcf().autofmt_xdate()   #自动调整日期显示的格式
        plt.xlabel('date')
        plt.ylabel('price')
    
        plt.show()
