#-------------------------------------------------------------------------------
# Name:        Stock Price Definition
# Purpose:
#
# Author:      Alan del Rio Mendez
#
# Created:     22/04/2013
# Copyright:   (c) Hewlett Packard
#-------------------------------------------------------------------------------

class FNStockPrice:
    def __init__(self,sDate,sTime,sSymbol,fPriceHigh,fPriceLow):
        self.__sDate=sDate
        self.__sTime=sTime
        self.__sSymbol=sSymbol
        self.__fPriceHigh=fPriceHigh
        self.__fPriceLow=fPriceLow
    def CSV(self):
        return self.__sDate+","+self.__sTime+","+self.__sSymbol+","+self.__fPriceHigh+","+self.__fPriceLow