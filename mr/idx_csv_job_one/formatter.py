#-------------------------------------------------------------------------------
# Name:       Formatter
# Purpose:
#
# Author:      Initial Version Created on MIT 
#              04/05/2013 - Alan del Rio - Define Cohesive Formmating Class
#
# Copyright:   (c) Hewlett Packard
#-------------------------------------------------------------------------------
#!/usr/bin/env python
from datetime import datetime
import re

def formatData(sFormat,sData):
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
    return newData
def format(doc):
    record = dict([])
    sData=""
    arrFields=[('DREREFERENCE','','doc'),
              ('DRETITLE','','doc'),
              ('AUTN_SOURCE','',''),
              ('CFSENDTIME','',''),
              ('CFSSTARTTIME','',''),
              ('DOCTRACKINGID','',''),
              ('DOCUMENTTRACKINGUUID','',''),
              ('DREDATE','DTZ','doc'),
              ('DREDATE_DAY','',''),
              ('DREDATE_HOUR','',''),
              ('DRELANGUAGETYPE','',''),
              ('EXPIRETIME','',''),
              ('FOLLOWERS','',''),
              ('FOLLOWING','',''),
              ('FROM_USER','',''),
              ('FROM_USER_ID','',''),
              ('FROM_USER_LINK','',''),
              ('FROM_USER_NAME','',''),
              ('INDEXTIME','',''),
              ('INTERACTION_AUTHOR_AVATAR','',''),
              ('INTERACTION_AUTHOR_ID','',''),
              ('INTERACTION_AUTHOR_LINK','',''),
              ('INTERACTION_AUTHOR_NAME','',''),
              ('INTERACTION_AUTHOR_USERNAME','',''),
              ('INTERACTION_CONTENT','','${DRECONTENT}'),
              ('INTERACTION_CREATED_AT','DSTZ',''),
              ('INTERACTION_ID','',''),
              ('INTERACTION_LINK','',''),
              ('INTERACTION_SCHEMA_VERSION','',''),
              ('INTERACTION_SOURCE','',''),
              ('INTERACTION_TYPE','',''),
              ('KLOUT_SCORE','',''),
              ('LANGUAGE_TAG_DISPLAYNAME','',''),
              ('LANGUAGE_CONFIDENCE','',''),
              ('LANGUAGE_TAG','',''),
              ('MAS_PROFILEGUID','',''),
              ('ORIGIN','',''),
              ('PROFILE_IMG','',''),
              ('SOURCE_DOMAIN','',''),
              ('SOURCEURL','',''),
              ('TWITTER_CREATED_AT','DSTZ',''),
              ('TWITTER_DOMAINS','',''),
              ('TWITTER_FILTER_LEVEL','',''),
              ('TWITTER_ID','',''),
              ('TWITTER_LINKS','',''),
              ('TWITTER_SOURCE','',''),
              ('TWITTER_TEXT','','${DRECONTENT}'),
              ('TWITTER_USER_CREATED_AT','DSTZ',''),
              ('TWITTER_USER_DESCRIPTION','',''),
              ('TWITTER_USER_FOLLOWERS_COUNT','',''),
              ('TWITTER_USER_FRIENDS_COUNT','',''),
              ('TWITTER_USER_ID','',''),
              ('TWITTER_USER_ID_STR','',''),
              ('TWITTER_USER_LANG','',''),
              ('TWITTER_USER_LISTED_COUNT','',''),
              ('TWITTER_USER_LOCATION','',''),
              ('TWITTER_USER_NAME','',''),
              ('TWITTER_USER_PROFILE_IMAGE_URL','',''),
              ('TWITTER_USER_SCREEN_NAME','',''),
              ('TWITTER_USER_STATUSES_COUNT','',''),
              ('TWITTER_USER_TIME_ZONE','',''),
              ('TWITTER_USER_UTC_OFFSET','',''),
              ('TYPE','',''),
              ('UPDATES','',''),
              ('STARTINDEXTASKSTIME','',''),
              ('SENTIMENT','',''),
              ('VIBE','',''),
              ('POSITIVE_VIBE_COUNT','',''),
              ('NEGATIVE_VIBE_COUNT','',''),
              ('MIXED_VIBE_COUNT','',''),
              ('SENTIMENT_NUMERIC','',''),
              ('POSITIVITY','',''),
              ('NEGATIVITY','',''),
              ('EXPORTJOBSTARTTIME','',''),
              ('EXPLOREINDEXTIME','',''),
              ('DRESECTION','','doc'),
              ('DREDBNAME','','doc')]

    
    for tupField in arrFields:
        sTemp=""
        if tupField[2] =="":
            if tupField[0] in doc.fields:
                sTemp=cleanData(doc.fields[tupField[0]])
        elif tupField[2] =="doc":
            if tupField[0] in doc.desc:
                sTemp=cleanData(doc.desc[tupField[0]])
        elif tupField[2] =="${DRECONTENT}":
                sTemp=cleanData(doc.desc['DRECONTENT'])

        if tupField[1] !="":
            #print tupField[0]+"###########################"+sTemp
            sTemp=formatData(tupField[1],sTemp)
        sData=sData+sTemp+"|"
    return sData[:-1]

def cleanData(sData):
        sData=sData.replace("\\n", "")
        sData=sData.replace("\n", "")
        sData=sData.replace("\r", "")
        sData=sData.replace("\\r", "")
        sData=sData.replace("|", "$")
        return sData