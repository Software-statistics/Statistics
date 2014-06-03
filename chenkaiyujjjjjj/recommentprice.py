from data import get_commodity_data

def recommentprice(asin):
    price_list=[]
    result=[]
    r=0.0
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
    average_price=r/len(price_list)
    lastest_price=price_list[-1]
    price_list.sort()
    lowest_price=price_list[0]
    result.append(average_price)
    result.append(lastest_price)
    result.append(lowest_price)
    #print average_price
    #print lastest_price
    #print lowest_price
    print result

if __name__ == '__main__':
    recommentprice('B003YUC4YI')
