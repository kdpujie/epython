'''
Created on 2015年11月12日

@author: pujie
'''

import logging
import pdb

logging.basicConfig(level=logging.INFO)  # 日志级别debug，info，warning，error


def division(dividend,divisor):
    try:
        print('starting...........')
        logging.info('n= %s' %divisor)
        r = int(dividend) / int(divisor)
        print('result:',r)
    except ValueError as e: # 把异常记录以后，往上抛
        logging.exception(e)   
        raise
    except ZeroDivisionError as e:
        logging.exception(e)
    else:# 如果没发生异常
        print('no error!')
    finally:
        print('finally......')
    print('.............END..................')


def main():
    print(division(10,2))


main()