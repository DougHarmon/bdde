#!/usr/bin/python
import re
import codecs
import stock_formatter

# Data stucture contains all infomation (precedent_timestamp, interval, and no_of_intervals) to calculate datetime, 
# and also the trading price
class Intraday_data(object):
    def __init__(self):
        self.interval = None
        self.precedent_timestamp = None
        self.no_of_intervals = None
        self.trading_price = None


def read_from_original(filename,callback=None):

    #INTERVAL=60
    interval_pattern = re.compile('^INTERVAL=(\d+)') 
    #a1364391000,456.7,456.8,456.41,456.46,106553
    firstDataLine_pattern = re.compile('^a(\d+),(.*)')
    #1,454.312,456.77,453.45,456.43,384917
    #2,455.25,455.34,454.04,454.31,152004
    #3,455.145,455.88,454.88,455.23,101717
    otherDataLine_pattern = re.compile('^(\d+),(.*)')
    
    with codecs.open(filename,'r','utf-8') as fin:
        interval = None
        precedent_timestamp = None
  
        for line in fin:
            m = otherDataLine_pattern.match(line)
            if m:
                data = Intraday_data()
                data.no_of_intervals = m.group(1)
                data.trading_price = m.group(2)
                data.interval = interval
                data.precedent_timestamp = precedent_timestamp
                callback(data)
                continue

            m = interval_pattern.match(line)
            if m:
                interval = m.group(1)
                continue

            m = firstDataLine_pattern.match(line)
            if m:
                precedent_timestamp = m.group(1)
                data = Intraday_data()
                data.precedent_timestamp = precedent_timestamp
                data.no_of_intervals = 0
                data.trading_price = m.group(2)
                data.interval = interval
                callback(data)
                continue

if __name__ == '__main__':
    formatter = stock_formatter.FormatCsv('output.cvs')
    read_from_original('AAPL_Mar26.csv', formatter)
    formatter.flush()