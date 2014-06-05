from data import get_commodity_data

def recommend_price(asin):
    price_list=[]
    result=[]
    r=0.0
    div=0
    data=get_commodity_data(asin)
    for offer in data['offer']:      
                for info in offer['info']:
                        try:
                                price_list.append(info['price'])
                        except:
                                pass
    #print price_list
    for i in price_list:
        r+=i
    if len(price_list)==0:
        div=1
    else:
        div=len(price_list)
    average_price=r/div
    lastest_price=price_list[-1]
    price_list.sort()
    lowest_price=price_list[0]
    result.append(average_price)
    result.append(lastest_price)
    result.append(lowest_price)
    #print average_price
    #print lastest_price
    #print lowest_price
    return result

