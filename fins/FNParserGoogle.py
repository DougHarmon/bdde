#-------------------------------------------------------------------------------
# Name:        FINS Google Stock Formatter
# Purpose:     Format Data to generate CSV
#
# Author:      Sizhong Yang Initial Version
#              alan.delrio@hp.com Cohesive Second Version
#
# Created:     22/04/2013
# Copyright:   (c) hpadmin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import re
from datetime import datetime
from FNStockPrice import FNStockPrice
class FNParserGoogle:
    def __init__(self,sSymbol):
        self.__sSymbol=sSymbol
    def recNormalized(self,prevDTS,iNoInt,iInt,iPriceH,iPriceL):
        dts = float(prevDTS) + float(iNoInt) * float(iInt)+10800
        ds = datetime.fromtimestamp(float(dts)).strftime("%Y-%m-%d")
        ts = datetime.fromtimestamp(float(dts)).strftime("%H:%M:%S")
        return FNStockPrice(ds,ts,self.__sSymbol,iPriceH,iPriceL)
    def parseData(self,dataLines):
        #INTERVAL=60
        interval_pattern = re.compile('^INTERVAL=(\d+)')
        #a1364391000,456.7,456.8,456.41,456.46,106553
        firstDataLine_pattern = re.compile('^a(\d+),(.*),(.*),(.*),(.*)')
        #1,454.312,456.77,453.45,456.43,384917
        #2,455.25,455.34,454.04,454.31,152004
        #3,455.145,455.88,454.88,455.23,101717
        otherDataLine_pattern = re.compile('^(\d+),(.*),(.*),(.*),(.*)')

        interval = None
        precedent_timestamp = None
        for line in dataLines:
            m = otherDataLine_pattern.match(line)
            if m:
                data = self.recNormalized(precedent_timestamp,m.group(1),interval,m.group(3),m.group(4))
                print data.CSV()
                continue

            m = interval_pattern.match(line)
            if m:
                interval = m.group(1)
                continue

            m = firstDataLine_pattern.match(line)
            if m:
                precedent_timestamp = m.group(1)
                data = self.recNormalized(precedent_timestamp,0,interval,m.group(3),m.group(4))
                print data.CSV()
                continue