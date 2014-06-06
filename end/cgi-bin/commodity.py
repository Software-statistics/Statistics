#!/usr/local/bin/python2.7

import cgi
import cgitb
import data
import singleprice
import singlecomment
import singlestar
import star
import recommend_goods
import recommendprice

cgitb.enable()
table = []

def addtable(table0):
	table.append(table0)
	
def getimgurl(asin='B003YUC4YI'):
	data0 = data.get_commodity_data(asin)
	imgurl = data0['productInfo'][0]['img']
	if '/mnt/mongo/ImageData/' in imgurl:
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

def commodity(asin):
	name = getname(asin)
	information = getinformation(asin)
	imgurl = getimgurl(asin)
	price = getprice(asin)
	
	recommend = recommend_goods.recommendcommodity(category)
	
	asin0=recommend[1]
	name0=getname(asin0)
	price0 = getprice(asin0)
	imgurl0 = getimgurl(asin0)
	
	asin1=recommend[2]
	name1=getname(asin1)
	price1 = getprice(asin1)
	imgurl1 = getimgurl(asin1)

	head='<!DOCTYPE HTML>'
	head+='<html><head>'
	head+='<title>software statistics</title>'
	head+='<link href="../css/commodity.css" rel="stylesheet" type="text/css" />'
	head+='''<script type="text/javascript" src="../jquery/jquery.min.js"></script>'''
	head+='''<script type="text/javascript" src="../highcharts/highcharts.js"></script>'''
	head+='''<script type="text/javascript" src="../highcharts/modules/exporting.js"></script>'''
	head+='''<script type="text/javascript" src="../highcharts/highcharts-more.js"></script>'''
	for each in table:
		head+=each
	head+='</head>'

	body='<body>'
	body+='<div id="logo">'
	body+='<h1 align="center">software statistics</h1>'
	body+='</div>'

	body+='<div id="page">'
	body+='<div id="page-bgtop">'
	body+='<table cellpadding="10" cellspacing="0" border="0" align="center">'
	body+='<tr>'
	body+='<table border="0" align="center">'
	body+='<tr>'
	body+='<td><img src="' + imgurl + '" /></td>'
	body+='<td><table id="informations" cellpadding="10" cellspacing="0" border="0" align="center">'
	body+='<tr><td><a href="http://www.amazon.com/dp/'+asin+'"><h3>'+name+'</h3></a></td></tr>'
	body+='<tr><td>$'+str(price)+'</td></tr>'
	body+='<tr><td>'+information+'</td></tr>'
	body+='</table></td>'
	body+='</tr>'
	body+='</table>'
	body+='</tr>'
	body+='<tr>'
	body+='<td>'
	body+='<div id="recommendinfo">'
	body+='<div style="width:920px;font-size:20px;margin:10px 0px 0px 20px;">recommended commodity:</div>'
	body+='<div id="recommend0">'
	body+='<div style="width:150px;height:150px;margin:10px 25px 0px 25px;">'
	body+='<a href="commodity.py?asin='+asin0+'&category='+category+'"><img src="' + imgurl0 + '" width="150px" height="150px" /></a>'
	body+='</div>'
	body+='<div style="width:170px;font-size:14px;margin:20px 10px 20px 20px;">'+name0+'</div>'
	body+='<div style="font-size:12px;margin:0px 0px 10px 40px;">$'+str(price0)+'</div>'
	body+='</div>'
	body+='<div id="recommend1">'
	body+='<div style="width:150px;height:150px;margin:10px 25px 0px 25px;">'
	body+='<a href="commodity.py?asin='+asin1+'&category='+category+'"><img src="' + imgurl1 + '" width="150px" height="150px" /></a>'
	body+='</div>'
	body+='<div style="width:170px;font-size:14px;margin:20px 10px 20px 20px;">'+name1+'</div>'
	body+='<div style="font-size:12px;margin:0px 0px 10px 40px;">$'+str(price1)+'</div>'
	body+='</div>'
	body+='<div id="speedstar"></div>'
	body+='</div>'
	
	body+='<div id="price"></div>'
	body+='<div id="comment"></div>'
	body+='<div id="star"></div>'
	
	body+='</td>'
	body+='</tr>'
	body+='</table>'
	body+='</div>'
	body+='</div>'
	body+='</body>'
	body+='</html>'
	return head+body

def commodity0(content='nothing'):
	
	head='<!DOCTYPE HTML>'
	head+='<html><head>'
	head+='<title>software statistics</title>'
	head+='</head>'
	body='<body>' +content+'</body>'
	body+='</html>'
	return head+body

form=cgi.FieldStorage()
asin=form.getvalue('asin')
category=form.getvalue('category')
#asin='B003YUC4YI'
addtable(singlestar.highchart(asin))
addtable(singleprice.highchart(asin))
addtable(singlecomment.highchart(asin))
addtable(star.highchart(asin))

print ("HTTP/1.0 200 OK")
print ("Content-Type: text/html")
print ("")
print ("")
print (commodity(asin))
