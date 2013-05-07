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
from FNFormatter import FNFormatter
import re
class FNTwFormatter(FNFormatter):
    def format(self,doc):
        arrFields=[('DREREFERENCE','','doc',0),
                    ('PROCESS_STATUS','','',1),
                    ('DRECONTENT','','doc',1),
                    ('ISO_LANG_CODE','','',1),
                    ('CREATED_ON','DSLASH','',1),
                    ('LOCATION','','',1),
                    ('GEO_LAT','','',1),
                    ('GEO_LONG','','',1),
                    ('AUTHOR_NAME','','',1),
                    ('SCORE','','',1),
                    ('STOCK','','',1),
                    ('EDKCOMPANY','','',1),
                    ('EDKPERSON','','',1),
                    ('EDKPLACE','','',1),
                    ('SENTIMENT_NEG','','',1),
                    ('SENTIMENT_POS','','',1),
                    ('SENTIMENT','','',1),
                    ('STOCK_TICKER','','',2),
                    ('SENTIMENT_NEG','','',2),
                    ('SENTIMENT_POS','','',2),
                    ('EDKCOMPANY','','',2),
                    ('EDKPERSON','','',2),
                    ('EDKPLACE','','',2)]
        return FNFormatter.format(self,doc,arrFields,"tweets")