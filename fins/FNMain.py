#-------------------------------------------------------------------------------
# Name:        Financial Main
# Purpose:     Download Stock Prices for Discover Demo
#
# Author:      Alan del Rio / alan.delrio@hp.com
#
# Created:     21/04/2013
# Copyright:   (c) Hewlett Packard
#-------------------------------------------------------------------------------
import urllib2
import FNStreamer
from FNParserGoogle import FNParserGoogle
class FNMain:
    __Symbols=[('Pepsi','PEP','GOOGLE'),
                ('Apple','AAPL','GOOGLE'),
                ('Starbucks','SBUX','GOOGLE'),
                ('Nike','NKE','GOOGLE'),
                ('Verizon','VZ','GOOGLE'),
                ('American Airlines','AAMRQ','GOOGLE'),
                ('Boeing','BA','GOOGLE'),
                ('DELL','DELL','GOOGLE'),
                ('Citigroup','C','GOOGLE'),
                ('Goldman Sachs','GS','GOOGLE'),
                ('IBM','IBM','GOOGLE'),
                ('Bank of America','BAC','GOOGLE'),
                ('American Express','AXP','GOOGLE'),
                ('BlackRock','BLK','GOOGLE'),
                ('Capital One','COF','GOOGLE'),
                ('Chipolte Mexican','CMG','GOOGLE'),
                ('NewMarket Corp','NEU','GOOGLE'),
                ('BankofCyprus','BOC','GOOGLE'),
                ('Cyprus popular bank','CPB','GOOGLE')]
    __FN_DS_Google="http://www.google.com/finance/getprices?i=60&p=15d&f=d,o,h,l,c,v&df=cpct&q=";
    __FN_DS_Yahoo=""
    __FN_DS=[]

    def __init__(self):
        for tupSymbol in self.__Symbols:
            if tupSymbol[2]=='GOOGLE':
                self.__FN_DS.append((self.__FN_DS_Google+tupSymbol[1],FNParserGoogle(tupSymbol[1])))
    def start(self):
        for tupDS in self.__FN_DS:
            objStream=FNStreamer.FNStreamer(tupDS)
            objStream.downloadData()

def main():
    objFNMain=FNMain()
    objFNMain.start()

if __name__ == '__main__':
    main()
