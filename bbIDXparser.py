import os
import document as idoc
import codecs
from datetime import datetime
from datetime import timedelta
from pprint import pprint
import re
import math



"""
Extract useful fields for the basketball project, from the IDX file, and write to a CSV file
"""
class ConvertToIdx(object):
    def __init__(self,dest_filename):
        self._dest_filename = dest_filename
        self._seen_references = set([])
        self._cache = []

        self._numberPositiveVibe=0
        self._numberNegativeVibe=0
        self._numberNeutralVibe=0
        self._numberTweets=0
        self._numberlatlongTweets=0
        self._numberlocationTweets=0
        self._numberPlayerTweets=0
        self._numberTeamTweets=0


    def __call__(self,doc):
        record = dict([])

        self._numberTweets = self._numberTweets + 1
        
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
            self._numberlatlongTweets = self._numberlatlongTweets + 1

        record['POSITIVE_VIBE'] = doc.fields['POSITIVE_PERCENT_VIBE']        
        record['NEGATIVE_VIBE'] = doc.fields['NEGATIVE_PERCENT_VIBE']
        record['NEUTRAL_VIBE'] = doc.fields['NEUTRAL_PERCENT_VIBE']

        if (int(record['POSITIVE_VIBE']) > 0):
            self._numberPositiveVibe = self._numberPositiveVibe + 1
        if (int(record['NEGATIVE_VIBE']) > 0):
            self._numberNegativeVibe = self._numberNegativeVibe + 1
        if (int(record['NEUTRAL_VIBE']) > 0):
            self._numberNeutralVibe = self._numberNeutralVibe + 1
        


        record['LOCATION'] = ""
        if 'USER_LOCATION' in doc.fields:
            record['LOCATION'] = doc.fields['USER_LOCATION']
            self._numberlocationTweets = self._numberlocationTweets + 1
        record['TEAM'] = ""
        if 'TEAM' in doc.fields:
            record['TEAM'] = doc.fields['TEAM']
            self._numberTeamTweets = self._numberTeamTweets + 1
        record['PLAYER'] = ""
        if 'PLAYER' in doc.fields:
            record['PLAYER'] = doc.fields['PLAYER']
            self._numberPlayerTweets = self._numberPlayerTweets + 1
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

        
        if not doc.reference in self._seen_references:
            self._cache.append(record)
            self._seen_references.add(doc.reference)
                
        if len(self._cache) >= 1000:
            print("Appending CSV file...  Total tweets = "+str(self._numberTweets))
            self.flush()


    def flush(self):
        with codecs.open(self._dest_filename, 'a', encoding='utf-8') as fout:
            for record in self._cache:
                fout.write('timestamp={0},utcOffset={1},location={2},lat={3},lon={4},lang={5},numberFollowers={6},numberStatuses={7},text={8},topic={9},vibePos={10},vibeNeg={11},vibeNeut={12},sentiment={13},team={14},player={15}\n'.format(record['TIMESTAMP'],record['USER_UTC_OFFSET'],record['LOCATION'],record['LATITUDE'],record['LONGITUDE'],record['USER_LANG'],record['USER_FOLLOWERS_COUNT'],record['USER_STATUSES_COUNT'],record['DRECONTENT'],record['TOPIC'],record['POSITIVE_VIBE'],record['NEGATIVE_VIBE'],record['NEUTRAL_VIBE'],record['SENTIMENT'],record['TEAM'],record['PLAYER']))
        self._cache = []



if __name__ == '__main__':
    convert = ConvertToIdx('C:\\Users\\fothergs\\Documents\\NCAA March Madness\\FinalTake_20130226160000\\ncaaMM.cvs')
    idoc.read_from_idx('C:\\Users\\fothergs\\Documents\\NCAA March Madness\\FinalTake_20130226160000\\ncaaMM_0_teams_players.idx', convert)
    idoc.read_from_idx('C:\\Users\\fothergs\\Documents\\NCAA March Madness\\FinalTake_20130226160000\\ncaaMM_1_teams_players.idx', convert)
    idoc.read_from_idx('C:\\Users\\fothergs\\Documents\\NCAA March Madness\\FinalTake_20130226160000\\ncaaMM_2_teams_players.idx', convert)
    idoc.read_from_idx('C:\\Users\\fothergs\\Documents\\NCAA March Madness\\FinalTake_20130226160000\\ncaaMM_3_teams_players.idx', convert)
    idoc.read_from_idx('C:\\Users\\fothergs\\Documents\\NCAA March Madness\\FinalTake_20130226160000\\ncaaMM_4_teams_players.idx', convert)
    convert.flush()
    print('There are '+str(convert._numberTweets)+' tweets')
    print("%.3d percent of tweets had a positive vibe" % (convert._numberPositiveVibe/convert._numberTweets*100))
    print("%.3d percent of tweets had a neutral vibe" % (convert._numberNeutralVibe/convert._numberTweets*100))
    print("%.3d percent of tweets had a negative vibe" % (convert._numberNegativeVibe/convert._numberTweets*100))
    print("There are %d tweets (%.3d) with lat + long information" % (convert._numberlatlongTweets, convert._numberlatlongTweets/convert._numberTweets*100))
    print("There are %d tweets (%.3d) that have a location" % (convert._numberlocationTweets, convert._numberlocationTweets/convert._numberTweets*100))
    print("There are %d tweets (%.3d) that contain team name information" % (convert._numberTeamTweets, convert._numberTeamTweets/convert._numberTweets*100))
    print("There are %d tweets (%.3d) that contain player name information" % (convert._numberPlayerTweets, convert._numberPlayerTweets/convert._numberTweets*100))
    print("There are %d tweets (%.3d) that have a location" % (convert._numberlocationTweets, convert._numberlocationTweets/convert._numberTweets*100))
