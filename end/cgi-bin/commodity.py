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
	return imgurl
	
def getinformation(asin='B003YUC4YI'):
	data0 = data.get_commodity_data(asin)
	information = data0['productInfo'][0]['productDescription']
	return information
	
def getname(asin='B003YUC4YI'):
	data0 = data.get_commodity_data(asin)
	name = data0['productInfo'][0]['name']
	return name

def commodity(asin):
	name = getname(asin)
	information = getinformation(asin)
	imgurl = getimgurl(asin)

	head='<!DOCTYPE HTML>'
	head+='<html><head>'
	head+='<title>software statistics</title>'
	head+='<link href="../css/commodity.css" rel="stylesheet" type="text/css" media="screen" />'
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
	body+='<table cellpadding="10" cellspacing="0" border="0" align="center">'
	body+='<tr>'
	body+='<table border="0" align="center">'
	body+='<tr>'
	body+='<td><img src="' + imgurl + '" /></td>'
	body+='<td><table id="informations" cellpadding="10" cellspacing="0" border="0" align="center">'
	body+='<tr><td><a href="http://www.amazon.com/dp/'+asin+'"><h3>'+name+'</h3></a></td></tr>'
	body+='<tr><td>'+information+'</td></tr>'
	body+='</table></td>'
	body+='</tr>'
	body+='</table>'
	body+='</tr>'
	body+='<tr>'
	body+='<td>'
	body+='<ul>'
	body+='<li>'
	body+='<div id="price" class="div-inline"></div><div id="comment" class="div-inline"></div>'
	body+='</li>'
	body+='<li>'
	body+='<div id="star"class="div-inline"></div>'
	body+='</li>'
	body+='</ul>'
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
#asin='B003YUC4YI'
addtable(singlestar.highchart(asin))
addtable(singleprice.highchart(asin))
addtable(singlecomment.highchart(asin))

print ("HTTP/1.0 200 OK")
print ("Content-Type: text/html")
print ("")
print ("")
print (commodity(asin))
