#-------------------------------------------------------------------------------
# Name:        Reducer
# Purpose:
#
# Author:      Initial Version Created on MIT 
#              04/05/2013 - Alan del Rio - Created to skip duplicates due bug on
#              XML Parsing class
#
# Copyright:   (c) Hewlett Packard
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys
prev_key = 'b'
if __name__ == '__main__':
    for line in sys.stdin:
    #compare the keys
        if line != prev_key:
            prev_key = line
            print line,