
def indexpage():
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

def head():
  head='<!DOCTYPE HTML>'
  head+='<html><head>'
  head+='<title>software statistics</title>'
  head+='</head>'
  return head
  
def body0():
	body='<body>'
	body+='<h1 align="center">software statistics</h1>'
	body+='<html:form name="input" action="/" method="post">'
	body+='First :<input type="text" name="catalogue0">'
	body+='Second :<input type="text" name="catalogue1">'
	body+='Third :<input type="text" name="catalogue2">'
	body+='<input type="submit" value="Submit">'
	body+='</html:form>'
	body+='</body>'
	return body
  
def body(content):
  body='<body>' +content+'</body>'
  return body
  
def foot():
	foot='</html>'
	return foot