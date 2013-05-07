#-------------------------------------------------------------------------------
# Name:        Web IDX to CSV
# Purpose:     Parse IDX generated from the web to generate a CSV equivalent
#
# Author:      Alan del Rio - alan.delrio@hp.com
#
# Created:     29/04/2013
# Copyright:   (c) Hewlett Packard - IMA
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
