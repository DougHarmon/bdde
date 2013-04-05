#-------------------------------------------------------------------------------
# Name:       Formatter
# Purpose:
#
# Author:      Initial Version Created on MIT 
#              04/05/2013 - Alan del Rio - Define Cohesive Formmating Class
#
# Copyright:   (c) Hewlett Packard
#-------------------------------------------------------------------------------
from datetime import datetime
import re

def format(doc):
    record = dict([])

    record['DRECONTENT'] = doc.content
    record['DRECONTENT'] = re.sub('\s', ' ', record['DRECONTENT'])

    created_at = doc.fields['CREATED_AT']
    dt = datetime.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y')
    record['TIMESTAMP'] = '{0}-{1:02}-{2:02}T{3:02}:{4:02}:{5:02}'.format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

    record['LONGITUDE'] = ''
    record['LATITUDE'] = ''
    if 'PLACE_BOUNDING_BOX_COORDINATES_COORDINATES_COORDINATES' in doc.fields:
        x0 = doc.fields['PLACE_BOUNDING_BOX_COORDINATES_COORDINATES_COORDINATES']
        y0 = doc.fields['PLACE_BOUNDING_BOX_COORDINATES_COORDINATES_COORDINATES1']
        y1 = doc.fields['PLACE_BOUNDING_BOX_COORDINATES_COORDINATES_COORDINATES111']
        x1 = doc.fields['PLACE_BOUNDING_BOX_COORDINATES_COORDINATES_COORDINATES1111']
        record['LONGITUDE'] = (float(x0)+float(x1))/2
        record['LATITUDE'] = (float(y0)+float(y1))/2

    record['POSITIVE_VIBE'] = doc.fields['POSITIVE_PERCENT_VIBE']
    record['NEGATIVE_VIBE'] = doc.fields['NEGATIVE_PERCENT_VIBE']
    record['NEUTRAL_VIBE'] = doc.fields['NEUTRAL_PERCENT_VIBE']

    record['LOCATION'] = ""
    if 'USER_LOCATION' in doc.fields:
        record['LOCATION'] = doc.fields['USER_LOCATION']
    record['TEAM'] = ""
    if 'TEAM' in doc.fields:
        record['TEAM'] = doc.fields['TEAM']
    record['PLAYER'] = ""
    if 'PLAYER' in doc.fields:
        record['PLAYER'] = doc.fields['PLAYER']
    record['VICTOR'] = ""
    if 'VICTOR' in doc.fields:
        record['VICTOR'] = doc.fields['VICTOR']
    record['LOSER'] = ""
    if 'LOSER' in doc.fields:
        record['LOSER'] = doc.fields['LOSER']
    record['SENTIMENT'] = ""
    if 'SENTIMENT' in doc.fields:
        record['SENTIMENT'] = doc.fields['SENTIMENT']
    record['TOPIC'] = ""
    if 'TOPIC' in doc.fields:
        record['TOPIC'] = doc.fields['TOPIC']

    record['RETWEET_COUNT'] = doc.fields['RETWEET_COUNT']
    record['USER_FOLLOWERS_COUNT'] = doc.fields['USER_FOLLOWERS_COUNT']
    record['USER_LANG'] = doc.fields['USER_LANG']
    record['USER_STATUSES_COUNT'] = doc.fields['USER_STATUSES_COUNT']
    record['USER_UTC_OFFSET'] = doc.fields['USER_UTC_OFFSET']


    record['POSITIVITY'] = doc.fields['POSITIVITY']
    record['SENTIMENTALITY'] = doc.fields['SENTIMENTALITY']
    record['INDICATES_VIBE'] = doc.fields['INDICATES_VIBE']
    record['POSITIVE_VIBE_TXT'] = ""
    if 'POSITIVE_VIBE' in doc.fields:
        record['POSITIVE_VIBE_TXT'] = doc.fields['POSITIVE_VIBE']
    record['NEGATIVE_VIBE_TXT'] = ""
    if 'NEGATIVE_VIBE' in doc.fields:
        record['NEGATIVE_VIBE_TXT'] = doc.fields['NEGATIVE_VIBE']

    return 'timestamp={0},utcOffset={1},location={2},lat={3},lon={4},lang={5},numberFollowers={6},numberStatuses={7},text={8},topic={9},vibePos={10},vibeNeg={11},vibeNeut={12},sentiment={13},team={14},player={15}\n'.format(record['TIMESTAMP'],record['USER_UTC_OFFSET'],record['LOCATION'],record['LATITUDE'],record['LONGITUDE'],record['USER_LANG'],record['USER_FOLLOWERS_COUNT'],record['USER_STATUSES_COUNT'],record['DRECONTENT'],record['TOPIC'],record['POSITIVE_VIBE'],record['NEGATIVE_VIBE'],record['NEUTRAL_VIBE'],record['SENTIMENT'],record['TEAM'],record['PLAYER'])