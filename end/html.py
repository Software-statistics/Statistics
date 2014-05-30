from data import get_commodity_data

table = []

def indexpage0():
	page='<!DOCTYPE HTML>'
	page+='<html><head>'
	page+='<title>software statistics</title>'
	page+='</head>'
	page+='<body>'
	page+='<h1 align="center">software statistics</h1>'
	page+='<form name="input" action="/" method="post" align="center">'
	page+='First :<input type="text" name="catalogue0">'
	page+='Second :<input type="text" name="catalogue1">'
	page+='Third :<input type="text" name="catalogue2">'
	page+='<input type="submit" value="Submit">'
	page+='</form>'
	page+='</body>'
	page+='</html>'
	return page
	
def indexpage():
	page='<!DOCTYPE HTML>'
	page+='<html><head>'
	page+='<title>software statistics</title>'
	page+='</head>'
	page+='<body>'
	page+='<h1 align="center">software statistics</h1>'
	page+='<form name="input" action="/" method="post" align="center">'
	page+='<label for="first">First :  </label>'
	page+='<select name="first" id="first">'
	page+='<option value="Shoes">Shoes</option>'
	page+='</select>'
	page+='<label for="second"> Second :  </label>'
	page+='<select name="second" id="second">'
	page+='<option value="Boys">Boys</option>'
	page+='<option value="Girls">Girls</option>'
	page+='</select>'
	page+='<label for="third"> Third :  </label>'
	page+='<select name="third" id="third" >'
	page+='<option value="Outdoor">Outdoor</option>'
	page+='</select>'
	page+='<input type="submit" value="Submit">'
	page+='</form>'
	page+='</body>'
	page+='</html>'
	return page

def head():
	head='<!DOCTYPE HTML>'
	head+='<html><head>'
	head+='<title>software statistics</title>'
	head+='''<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>'''
	head+='''<script type="text/javascript" src="http://code.highcharts.com/highcharts.js"></script>'''
	for each in table:
		head+=each
	head+='</head>'
	return head
  
def body0(asin):
	name = getname(asin)
	information = getinformation(asin)
	imgurl = getimgurl(asin)

	css='<style type = "text/css" >'
	css+='#informations a:hover{'
	css+='background-color:yellow;'
	css+='}'
	css+='#informations a:link{'
	css+='text-decoration:none;'
	css+='}'
	css+='#price{'
	css+='height:300px;'
	css+='width:750px;'
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
	body+='<div id="price"></div>'
	body+='</li>'
	body+='</ul>'
	body+='</td>'
	body+='</tr>'
	body+='</table>'
	body+='</body>'
	return css+body
	
def addtable(table0):
	table.append(table0)
  
def body(content='nothing'):
	body='<body>' +content+'</body>'
	return body
  
def foot():
	foot='</html>'
	return foot
	
def getimgurl(asin='B003YUC4YI'):
	data = get_commodity_data(asin)
	imgurl = data['productInfo'][0]['img']
	return imgurl
	
def getinformation(asin='B003YUC4YI'):
	data = get_commodity_data(asin)
	information = data['productInfo'][0]['productDescription']
	return information
	
def getname(asin='B003YUC4YI'):
	data = get_commodity_data(asin)
	print data['productInfo']
	name = data['productInfo'][0]['name']
	return name
