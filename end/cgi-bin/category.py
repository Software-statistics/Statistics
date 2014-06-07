#!/usr/local/bin/python2.7

import cgi
import cgitb
import data
import allstar
import recommendprice
import recommend_goods

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
	return recommendprice.recommend_price(asin)[1]
	
def category(category,i):
	data0=data.get_category_page(category,i)
	
	recommend = recommend_goods.recommendcommodity(category)
	
	
	head='<!DOCTYPE HTML>'
	head+='<html><head>'
	head+='<title>software statistics</title>'
	head+='<link href="../css/category.css" rel="stylesheet" type="text/css" />'
	head+='''<script type="text/javascript" src="http:../jquery/jquery.min.js"></script>'''
	head+='''<script type="text/javascript" src="../highcharts/highcharts.js"></script>'''
	for each in table:
		head+=each
	head+='</head>'
	
	
	body='<body>'
	body+='<div id="logo">'
	body+='<h1 align="center">software statistics</h1>'
	body+='</div>'
	body+='<div id="page">'
	body+='<div id="page-bgtop">'
	body+='<div style="width:920px;font-size:32px;margin:0px 0px 30px 20px;">'
	body+=category
	body+='</div>'
	
	asin0=recommend[0]
	name0=getname(asin0)
	price0 = getprice(asin0)
	imgurl0 = getimgurl(asin0)
	
	body+='<div style="width:920px;height:300px;">'
	body+='<div style="width:500px;height:240px;margin:30px 0px 0px 0px;float:left;">'
	body+='<div style="width:500px;height:30px;font-size:26px;margin:10px 0px 0px 20px;">most popular:</div>'
	body+='<div style="width:190px;height:190px;float:left;margin:5px 5px 5px 5px;">'
	body+='<a href="commodity.py?asin='+asin0+'&category='+category+'"><img src="' + imgurl0 + '" width="190px" height="190px" /></a>'
	body+='</div>'
	body+='<div style="width:300px;height:180px;float:left;margin:20px 0px 0px 0px;">'
	body+='<div style="width:270px;font-size:18px;margin:20px 10px 20px 20px;">'+name0+'</div>'
	body+='<div style="font-size:16px;margin:0px 0px 10px 40px;">$'+str(price0)+'</div>'
	body+='</div>'
	body+='</div>'
	
	body+='<div id="allstar" style="width:400px;height:300px;float:left;"></div>'
	body+='</div>'	
	for each in data0:
		asin=each['ASIN']
		name = getname(asin)
		price = getprice(asin)
		imgurl = getimgurl(asin)
		
		body+='<div style="width:800px;height:110px;border:groove 2px grey;margin:5px 50px 5px 50px;">'
		body+='<div class="pic" style="width:100px;height:100px;float:left;margin:5px 5px 5px 20px;">'
		body+='<a href="commodity.py?asin='+asin+'&category='+category+'"><img src="' + imgurl + '" width="100px" height="100px" /></a>'
		body+='</div>'
		body+='<div class="info" style="width:600px;height:110px;float:left;margin:0px 20px 0px 20px;">'
		body+='<div style="width:560px;font-size:18px;margin:20px 5px 20px 10px;">'+name+'</div>'
		body+='<div style="font-size:14px;margin:0px 50px 10px 20px;">$'+str(price)+'</div>'
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
addtable(allstar.highchart(category0))

print ("HTTP/1.0 200 OK")
print ("Content-Type: text/html")
print ("")
print ("")
#print ("<p>%s</p>" % (category0))
print (category(category0,1))
