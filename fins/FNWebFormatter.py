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
import time
import re
class FNWebFormatter(FNFormatter):
    def format(self,doc):
        arrFields=[('DREREFERENCE','','doc',0),
                    ('DREDATE','EPOCH','doc',1),
                    ('STOCK_TICKER','','',1),
                    ('ISO_LANGUAGE_CODE','','',1),
                    ('KEYWORDS','','',1),
                    ('SOURCEURL','','',1),
                    ('SPIDERDOMAIN','','',1),
                    ('DRETITLE','','doc',1),
                    ('TITLE','','',1),
                    ('TYPE','','',1),
                    ('SENTIMENT','','',1),
                    ('VIBE','','',1),
                    ('DREDBNAME','','doc',1),
                    ('SENTIMENT_POS','','',2),
                    ('SENTIMENT_NEG','','',2),
                    ('EDKPERSON','','',2),
                    ('EDKPLACE','','',2),
                    ('EDKCOMPANY','','',2)]
        return FNFormatter.format(self,doc,arrFields,"web")