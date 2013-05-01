#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hpadmin
#
# Created:     29/04/2013
# Copyright:   (c) hpadmin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
from IDXParser import IDXParser
from FNWebFormatter import FNWebFormatter

class FNWritter:
    def write(self,sData):
        print sData

class TwIdxVertica:
    def main(self):
        objIdxParser=IDXParser(FNWebFormatter(),FNWritter())
        objIdxParser.parseIDX(sys.stdin)

if __name__ == '__main__':
    objTwIdx=TwIdxVertica()
    objTwIdx.main()
