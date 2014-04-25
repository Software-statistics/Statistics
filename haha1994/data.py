import urllib
import simplejson as json

REQUEST_URL = 'http://112.124.1.3:8004'

def get_data():
        all_c = 'api/commodity/'
        sort = 'Shoes>Boys>Outdoor'
        #sort = raw_input("please input the category,for example Shoes>Boys>Outdoor")

        data = json.loads(urllib.urlopen('?'.join([('/'.join([REQUEST_URL,all_c])),urllib.urlencode({'category_name':sort})])).read())
        return data

def get_commodity_data(asin):
        all_c = 'api/commodity/'
       
        data = json.loads(urllib.urlopen(''.join([('/'.join([REQUEST_URL,all_c])),asin])).read())
        return data
