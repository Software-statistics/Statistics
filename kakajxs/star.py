#-*- coding:utf-8 -*-

import urllib
import simplejson as json
import matplotlib.pyplot as plt
from datetime import datetime
from data import get_commodity_data

def getstar(asin):

        data = get_commodity_data(asin)
        star=float(data['stats_info']['avg_info'])
        result=str(star)
        print result
        return result

def highchart(asin):
        star = getstar(asin)
        print star
        #content='''<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>'''
        #content+='''<script type="text/javascript" src="http://code.highcharts.com/highcharts.js"></script>'''

        content='''<script type="text/javascript" src="js/jquery.min.js"></script>
  <script type="text/javascript" src="js/highcharts.js"></script>
  <script type="text/javascript" src="js/exporting.js"></script>
  <script type="text/javascript" src="js/highcharts-more.js"></script>'''
        content+='''<script>'''
        content+='''$(function () {'''
	content+='''$('#container').highcharts({'''
	content+='''chart: {'''
	content+='''type: 'gauge','''
	content+='''plotBackgroundColor: null,'''
	content+='''plotBackgroundImage: null,'''
	content+='''plotBorderWidth: 0,'''
	content+='''plotShadow: false'''
	content+='''},'''
	content+='''title: {'''
	content+='''text: 'Star' '''
	content+='''},'''
	content+='''pane: {'''
	content+='''startAngle: -150,'''
	content+='''endAngle: 150,'''
	content+='''background: [{'''
	content+='''backgroundColor: {'''
	content+='''linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },'''
	content+='''stops: ['''
	content+='''[0, '#FFF'],'''
	content+='''[1, '#333']'''
	content+=''']'''
	content+='''},'''
	content+='''borderWidth: 0,'''
	content+='''outerRadius: '109%' '''
	content+='''}, {'''
	content+='''backgroundColor: {'''
	content+='''linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },'''
	content+='''stops: ['''
	content+='''[0, '#333'],'''
	content+='''[1, '#FFF']'''
	content+=''']'''
	content+='''},'''
	content+='''borderWidth: 1,'''
	content+='''outerRadius: '107%' '''
	content+='''}, {'''
	content+='''// default background'''
	content+='''}, {'''
	content+='''backgroundColor: '#DDD','''
	content+='''borderWidth: 0,'''
	content+='''outerRadius: '105%','''
	content+='''innerRadius: '103%' '''
	content+='''}]'''
	content+='''},'''
	content+='''// the value axis'''
	content+='''yAxis: {'''
	content+='''min: 0,'''
	content+='''max: 5,'''
	content+='''minorTickInterval: 'auto','''
	content+='''minorTickWidth: 1,'''
	content+='''minorTickLength: 10,'''
	content+='''minorTickPosition: 'inside','''
	content+='''minorTickColor: '#666','''
	content+='''tickPixelInterval: 30,'''
	content+='''tickWidth: 2,'''
	content+='''tickPosition: 'inside','''
	content+='''tickLength: 10,'''
	content+='''tickColor: '#666','''
	content+='''labels: {'''
	content+='''step: 2,'''
	content+='''rotation: 'auto' '''
	content+='''},'''
	content+='''title: {'''
	content+='''text: 'star' '''
	content+='''},'''
	content+='''plotBands: [{'''
	content+='''from: 0,'''
	content+='''to: 1,'''
	content+='''color: '#55BF3B' // green'''
	content+='''}, {'''
	content+='''from: 1,'''
	content+='''to: 2,'''
	content+='''color: '#DDDF0D' // yellow'''
	content+='''}, {'''
	content+='''from: 2,'''
	content+='''to: 3,'''
	content+='''color: '#DF5353' // red'''
	content+='''}, {'''
	content+='''from: 3,'''
	content+='''to: 4,'''
	content+='''color: '#DDDF0D' // yellow'''
	content+='''}, {'''
	content+='''from: 4,'''
	content+='''to: 5,'''
	content+='''color: '#55BF3B' '''
	content+='''}]'''
	content+='''},'''
	content+='''series: [{'''
	content+='''name: 'Speed','''
	content+='''data: ['''
	content+=star
	content+='''],'''
	content+='''tooltip: {'''
	content+='''valueSuffix: ' star' '''
	content+='''}'''
	content+='''}]'''
	content+='''}, '''
	#content+='''// Add some life'''
	content+='''function (chart) {'''
	content+='''if (!chart.renderer.forExport) {'''
	content+='''setInterval(function () {'''
	content+='''var point = chart.series[0].points[0],'''
	content+='''newVal,'''
	content+='''inc = 0;'''        
	content+='''newVal = point.y + inc;'''
	content+='''if (newVal < 0 || newVal > 200) {'''
        content+='''newVal = point.y - inc;'''
	content+='''}'''
	content+='''point.update(newVal);'''  
	content+='''}, 3000);'''
	content+='''}'''
	content+='''});'''
        content+='''});'''
        content+='''</script>'''
        print content
        #content+='''<div id="container" style="min-width: 310px; height: 400px; margin: 0 auto"></div>'''
        return content
