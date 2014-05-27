#-*- coding:utf-8 -*-
from data import get_commodity_data
from star_count import starcount
from star_count import starcount0
from star_count import starcountall

if __name__ == '__main__':
        #Shoes>Boys>Outdoor
	#starcount('Shoes>Boys>Outdoor', 12)
        #B003YUC4YI
        #starcount0('B003YUC4YI')
        print 'nimei'
        data = get_commodity_data('B003YUC4YI')
        print 'nimei'
        print data
        print 'nimei'
        #starcountall('Shoes>Boys>Outdoor')
