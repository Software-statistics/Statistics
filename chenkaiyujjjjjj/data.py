#-*- coding:utf-8 -*-
import urllib
import simplejson as json

REQUEST_URL = 'http://112.124.1.3:8004'
all_c = 'api/commodity/'

# 获取sort分类下第n个数据所在页
def get_category_data(sort, n):
        a = int(n/20)
        data = json.loads(urllib.urlopen('?'.join([('/'.join([REQUEST_URL,all_c])),urllib.urlencode({'category_name':sort ,'page':a})])).read())
        return data
        
# 获取特定商品编码数据			
def get_commodity_data(asin):
        data = json.loads(urllib.urlopen(''.join([('/'.join([REQUEST_URL,all_c])),asin])).read())
        return data
        
# 得到sort分类下商品的数量
def get_category_count(sort):
        data = json.loads(urllib.urlopen('?'.join([('/'.join([REQUEST_URL,all_c])),urllib.urlencode({'category_name':sort})])).read())
        return data['count']

# 得到sort分类下所有数据
def get_category_all(sort):
        n = get_category_count(sort)
        
        data = []
        
        for i in range(0,int(n/20)):
        	data.append(get_category_data(sort,i))
       
        return data

# 得到sort分类下field下的数据（第一页）
def get_commodity_field(sort,field):
        data = json.loads(urllib.urlopen('?'.join([('/'.join([REQUEST_URL,all_c])),urllib.urlencode({'category_name':sort ,'field':field})])).read())
        return data

# 得到sort分类下第n页的数据
def get_category_page(sort,page):
	data = json.loads(urllib.urlopen('?'.join([('/'.join([REQUEST_URL,all_c])),urllib.urlencode({'category_name':sort ,'page':page})])).read())
	return data