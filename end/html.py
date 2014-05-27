from data import get_commodity_data

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
	page+='<select name="first">'
	page+='First :<option value="Shoes">Shoes</option>'
	page+='</select>'
	page+='<select name="second">'
	page+='Second :<option value="Boys">Boys</option>'
	page+='<option value="Girls">Girls</option>'
	page+='</select>'
	page+='<select name="third">'
	page+='Third :<option value="Outdoor">Outdoor</option>'
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
  head+='</head>'
  return head
  
def body0(asin):
	name = getname(asin)
	information = getinformation(asin)
	imgurl = getimgurl(asin)
	css='<style type = "text/css" >'
	css+='#asinimg {'
	css+='width : 300px;'
	css+='height : 400px;'
	css+='}'
	css+='}'
	css+='</style>'

	body='<body>'
	body+='<h1 align="center">software statistics</h1>'
	body+='<table cellpadding="10" cellspacing="0" border="0" align="center">'
	body+='<tr>'
	body+='<td id="asinimg"><img src="' + imgurl + '" /></td>'
	body+='<td><table cellpadding="10" cellspacing="0" border="0" align="center">'
	body+='<tr><td>'+name+'</td></tr>'
	body+='<tr><td>'+information+'</td></tr>'
	body+='</table></td>'
	body+='</tr>'
	body+='</table>'
	body+='</body>'
	return css+body
  
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