#-------------------------------------------------------------------------------
# Name:       LCI Twitter Formatter
# Purpose:
#
# Author:      Initial Version Created on MIT
#              04/05/2013 - Alan del Rio - Define Cohesive Formmating Class
#
# Copyright:   (c) Hewlett Packard
#-------------------------------------------------------------------------------
#!/usr/bin/env python
from datetime import datetime
import time
import re
class FNWebFormatter:
    def formatData(self,sFormat,sData):
        newData=""
        if sData!="":
            if sFormat=="DSTZ":
                #DREFIELD TWITTER_CREATED_AT="Mon, 25 Mar 2013 13:05:52 +0000"
                arrDate=sData.split(' ')
                if len(arrDate)>5:
                    dt = datetime.strptime(arrDate[0]+" "+arrDate[1]+" "+arrDate[2]+" "+arrDate[3]+" "+arrDate[4], '%a, %d %b %Y %H:%M:%S')
                    newData = "{0}-{1:02d}-{2:02d} {3:02d}:{4:02d}:{5:02d}.0".format(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second)
            if sFormat=="DTZ":
                arrDate=sData.split(' ')
                if len(arrDate)>1:
                    #2013-03-25 13:05:52 +0000 -.rstrip("0")
                    newData =arrDate[0]+" "+arrDate[1]+".0"
            if sFormat=="DSLASH":
                newData=sData.replace("/","-")
            if sFormat=="EPOCH":
                newData=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(sData)))
        return newData
    def format(self,doc):
        record = dict([])
        sData=""
        arrFields=[('DREREFERENCE','','doc'),
                    ('DREDATE','EPOCH','doc'),
                    ('STOCK_TICKER','',''),
                    ('ISO_LANGUAGE_CODE','',''),
                    ('KEYWORDS','',''),
                    ('SOURCEURL','',''),
                    ('SPIDERDOMAIN','',''),
                    ('DRETITLE','','doc'),
                    ('TITLE','',''),
                    ('TYPE','',''),
                    ('SENTIMENT','',''),
                    ('VIBE','',''),
                    ('DREDBNAME','','doc')]

        for tupField in arrFields:
            sTemp=""
            if tupField[2] =="":
                if tupField[0] in doc.fields:
                    sTemp=self.cleanData(doc.fields[tupField[0]])
            elif tupField[2] =="doc":
                if tupField[0] in doc.desc:
                    sTemp=self.cleanData(doc.desc[tupField[0]])
            elif tupField[2] =="${DRECONTENT}":
                    sTemp=self.cleanData(doc.desc['DRECONTENT'])

            if tupField[1] !="":
                sTemp=self.formatData(tupField[1],sTemp)
            sData=sData+sTemp+"|"
        return sData[:-1]

    def cleanData(self,sData):
            sData=sData.replace("\\n", "")
            sData=sData.replace("\n", "")
            sData=sData.replace("\r", "")
            sData=sData.replace("\\r", "")
            sData=sData.replace("|", "$")
            return sData
