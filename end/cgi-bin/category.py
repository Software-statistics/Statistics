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
	head+='''<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>'''
	head+='''<script type="text/javascript" src="http://code.highcharts.com/highcharts.js"></script>'''
	for each in table:
		head+=each
	head+='</head>'

	css='<style type = "text/css" >'
	css+='#informations a:hover{'
	css+='background-color:yellow;'
	css+='}'
	css+='#informations a:link{'
	css+='text-decoration:none;'
	css+='}'
	css+='div{'
	css+='display:inline'
	css+='}'
	css+='#price{'
	css+='height:400px;'
	css+='width:600px;'
	css+='}'
	css+='#comment{'
	css+='height:400px;'
	css+='width:600px;'
	css+='}'
	css+='#star{'
	css+='height:400px;'
	css+='width:600px;'
	css+='}'
	css+='</style>'

	body='<body>'
	body+='<h1 align="center">software statistics</h1>'
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
	body+='<div id="price"></div><div id="comment"></div>'
	body+='</li>'
	body+='<li>'
	body+='<div id="star"></div>'
	body+='</li>'
	body+='</ul>'
	body+='</td>'
	body+='</tr>'
	body+='</table>'
	body+='</body>'
	body+='</html>'
	return head+css+body

def commodity0(content='nothing'):
	
	head='<!DOCTYPE HTML>'
	head+='<html><head>'
	head+='<title>software statistics</title>'
	head+='</head>'
	body='<body>' +content+'</body>'
	body+='</html>'
	return head+body

#addtable(singlestar.highchart('B003YUC4YI'))
addtable(singleprice.highchart('B003YUC4YI'))
addtable(singlecomment.highchart('B003YUC4YI'))
print ("HTTP/1.0 200 OK")
print ("Content-Type: text/html")
print ("")
print ("")
#print ("<p>hello</p>")
print (commodity('B003YUC4YI'))
