#-------------------------------------------------------------------------------
# Name:        Twitter Parser for
# Purpose:
#
# Author:      hpadmin
#
# Created:     28/04/2013
# Copyright:   (c) hpadmin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class CsvIdxParser:
    def __init__(self,tupMapping,sDel,iLenValidator):
        self.__tupMapping=tupMapping
        self.__sDel=sDel
        self.__iLenValidator=iLenValidator
        pass
    def formatVal(self,sData,sFunc):
        if sFunc=="trim":
            sData=sData.strip()
        return sData
    def parse(self,sLine):
        return self.mapping(sLine.split(self.__sDel))
    def mapping(self,arrElements):
        sIDX=""
        sVal=""
        if len(arrElements)>=self.__iLenValidator:
            for tupMap in self.__tupMapping:
                sVal=""
                for mapping in tupMap[2]:
                    sVal=sVal+arrElements[mapping]
                sVal=self.formatVal(sVal,tupMap[3])
                if tupMap[0]=="":
                    sField="#"+tupMap[1]+sVal+"\n";
                else:
    				sField="#"+tupMap[0]+' '+tupMap[1]+'="'+sVal+'"'+"\n";
                sIDX=sIDX+sField;
            sIDX=sIDX+"#DREENDDOC\n\n"
        return sIDX