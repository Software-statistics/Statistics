#!/usr/local/bin/python2.7

import cgi
import cgitb
import data
import singleprice
import singlecomment
import singlestar

cgitb.enable()
table = []
	
def addtable(table0):
	table.append(table0)
	
def getimgurl(asin='B003YUC4YI'):
	data0 = data.get_commodity_data(asin)
	imgurl = data0['productInfo'][0]['img']
	if imgurl==('/mnt/mongo/ImageData/'+first+'/'+second+'/'+third+'/'+asin+'.jpeg'):
			imgurl='../images/404.jpg'
	return imgurl
	
def getinformation(asin='B003YUC4YI'):
	data0 = data.get_commodity_data(asin)
	information = data0['productInfo'][0]['productDescription']
	return information
	
def getname(asin='B003YUC4YI'):
	data0 = data.get_commodity_data(asin)
	name = data0['productInfo'][0]['name']
	return name
	
def getprice(asin='B003YUC4YI'):
	return 100
	
def category(category,i):
	data0=data.get_category_page(category,i)
	
	
	head='<!DOCTYPE HTML>'
	head+='<html><head>'
	head+='<title>software statistics</title>'
	head+='<link href="../css/category.css" rel="stylesheet" type="text/css" />'
	head+='''<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>'''
	head+='''<script type="text/javascript" src="http://code.highcharts.com/highcharts.js"></script>'''
	for each in table:
		head+=each
	head+='</head>'
	
	
	body='<body>'
	body+='<div id="logo">'
	body+='<h1 align="center">software statistics</h1>'
	body+='</div>'
	body+='<div id="page">'
	body+='<div id="page-bgtop">'
	body+=category
	for each in data0:
		asin=each['ASIN']
		name = getname(asin)
		price = getprice(asin)
		imgurl = getimgurl(asin)
		
		body+='<div style="width:650px;height:110px">'
		body+='<div class="pic" style="width:110px;height:110px;float:left; display:inline">'
		body+='<a href="commodity.py?asin='+asin+'"><img src="' + imgurl + '" width="100px" height="100px" /></a>'
		body+='</div>'
		body+='<div class="info" style="width:500px;height:110px;float:left; display:inline">'
		body+='<div style="width:500px;">'+name+'</div>'
		body+='<div>'+str(price)+'</div>'
		body+='</div>'
		body+='</div>'
	body+='</div>'
	body+='</div>'
	body+='</body>'
	body+='</html>'
	return head+body
	
form=cgi.FieldStorage()
first=form.getvalue('first')
second=form.getvalue('second')
third=form.getvalue('third')
category0=first+'>'+second+'>'+third
#addtable(singlestar.highchart('B003YUC4YI'))
#addtable(singleprice.highchart('B003YUC4YI'))
#addtable(singlecomment.highchart('B003YUC4YI'))
print ("HTTP/1.0 200 OK")
print ("Content-Type: text/html")
print ("")
print ("")
#print ("<p>%s</p>" % (category0))
print (category(category0,1))
