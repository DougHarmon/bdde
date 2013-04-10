#!/usr/bin/env python
import sys
prev_key = 'b'
if __name__ == '__main__':
    for line in sys.stdin:
    #compare the keys
        if line != prev_key:
            prev_key = line
            print line,