#-------------------------------------------------------------------------------
# Name:        Financial Streamer
# Purpose:     Download Financial Data
#
# Author:      Alan del Rio / alan.delrio@hp.com
#
# Created:     21/04/2013
# Copyright:   (c) Hewlett Packard
#-------------------------------------------------------------------------------
import urllib2
class FNStreamer:
    def __init__(self,tupDS):
        self.__tupDS=tupDS;

    def downloadData(self):
        #print "Downloading Data "+self.__tupDS[0]
        response = urllib2.urlopen(self.__tupDS[0])
        self.__tupDS[1].parseData(response.readlines())