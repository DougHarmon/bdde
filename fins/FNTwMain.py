#-------------------------------------------------------------------------------
# Name:        Alan del Rio Mendez
# Purpose:     Configure and Trigger Twitter CSV to IDX Parsing
#
# Author:      hpadmin
#
# Created:     28/04/2013
# Copyright:   (c) hpadmin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from CsvIdxParser import CsvIdxParser
import sys
import time
from FileWritter import FileWritter

class FNTwitterMain:
    __mapping=[("","DREREFERENCE",{0,1},""),
             ("DREFIELD","PROCESS_STATUS",{2},""),
             ("DREFIELD","REVIEW_TEXT",{3},""),
             ("DREFIELD","ISO_LANG_CODE",{4},""),
             ("DREFIELD","CREATED_ON",{5},""),
             ("DREFIELD","LOCATION",{6},""),
             ("DREFIELD","GEO_LAT",{7},""),
             ("DREFIELD","GEO_LONG",{8},""),
             ("DREFIELD","AUTHOR_NAME",{9},""),
             ("DREFIELD","SCORE",{10},""),
            ("DREFIELD","STOCK",{11},"trim")]
    __sDel="\t"
    __bHeader=False
    __iLenValidator=12

    def main(self):
        objFileWritter=FileWritter("IDX_TW_"+time.strftime("%Y-%m-%d_%H_%M_%S")+".idx",1000)
        objParser=CsvIdxParser(self.__mapping,self.__sDel,self.__iLenValidator)
        for sLine in sys.stdin:
            slLine=sLine.replace("\r\n", "")
            slLine=sLine.replace("\n", "")
            if self.__bHeader==True:
                sRes=objParser.parse(sLine)
                if sRes!="":
                    objFileWritter.writeBuffered(sRes)
            else:
                self.__bHeader=True
        objFileWritter.flush()

if __name__ == '__main__':
    objTwMain=FNTwitterMain()
    objTwMain.main()