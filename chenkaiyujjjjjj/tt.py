from data import get_category_all 

def show(sort):
    data=get_category_all(sort)
    print data[0]['productInfo']

if __name__ == '__main__':
    show('Shoes>Boys>Outdoor')
    print ss
