import os
#import document as idoc
import codecs
from datetime import datetime
from datetime import timedelta
from pprint import pprint
import re
import math


"""
Extract useful fields for the basketball project, from the IDX file, and write to a CSV file
"""
class CSV(object):
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


    def __call__(self,record):
        #if not doc.reference in self._seen_references:
        #    self._cache.append(record)
        #    self._seen_references.add(doc.reference)

        self._cache.append(record)		
        if len(self._cache) >= 1000:
            print("Appending CSV file...  Total tweets = "+str(self._numberTweets))
            self.flush()


    def flush(self):
        with open(self._dest_filename, 'a') as fout:
            for record in self._cache:
                fout.write('timestamp={0},utcOffset={1},location={2},lat={3},lon={4},lang={5},numberFollowers={6},numberStatuses={7},text={8},topic={9},vibePos={10},vibeNeg={11},vibeNeut={12},sentiment={13},team={14},player={15}\n'.format(record['TIMESTAMP'],record['USER_UTC_OFFSET'],record['LOCATION'],record['LATITUDE'],record['LONGITUDE'],record['USER_LANG'],record['USER_FOLLOWERS_COUNT'],record['USER_STATUSES_COUNT'],record['DRECONTENT'],record['TOPIC'],record['POSITIVE_VIBE'],record['NEGATIVE_VIBE'],record['NEUTRAL_VIBE'],record['SENTIMENT'],record['TEAM'],record['PLAYER']))
        self._cache = []
