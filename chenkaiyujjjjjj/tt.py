from data import get_category_page

def show(sort,page):
    data=get_category_page(sort,page)
    print data[1]['productInfo'][0]['productDetail'][0]['bestSellerRank']

if __name__ == '__main__':
    show('Shoes>Boys>Outdoor',1)
