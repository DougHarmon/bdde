import os
import codecs
from datetime import datetime
from datetime import timedelta
from pprint import pprint
import re
import math

"""
Extract useful fields for the FINS Demo project, from a text file downloaded from google finance, and write to a CSV file
"""
class FormatCsv(object):
    def __init__(self,dest_filename):
        self._dest_filename = dest_filename
        self._cache = []
        self._numOfLines = 0

    def __call__(self,line):
        record = dict([])
        precedent_ts = line.precedent_timestamp
        curr_ts = float(line.precedent_timestamp) + float(line.no_of_intervals) * float(line.interval)
        record['datetime'] = datetime.fromtimestamp(float(curr_ts))
        record['price'] = line.trading_price
        
        self._cache.append(record)

        if len(self._cache) >= 1000:
            self.flush()


    def flush(self):
        with codecs.open(self._dest_filename, 'a', encoding='utf-8') as fout:
            for record in self._cache:
                fout.write('{0},{1}\n'.format(record['datetime'],record['price']))

        self._numOfLines = self._numOfLines + len(self._cache)
        print("Appending CSV file...  total intraday trading data:" + str(self._numOfLines))
        self._cache = []

