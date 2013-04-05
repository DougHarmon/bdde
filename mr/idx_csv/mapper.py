#!/usr/bin/env python 
import sys
import re
import formatter
class IDX(object):
    def __init__(self,reference):
        self.reference = reference
        self.fields = dict([])
        self.title = None
        self.date = None
        self.section = None
        self.db = None
        self.content = None

def parseIDX():
    """
    Parses an IDX file and generates an CSV representation of an IDX record
    sLine
    """
    results = []

    reference_pattern = re.compile('^#DREREFERENCE\s+(.+)')
    field_pattern = re.compile('^#DREFIELD\s+(.+)="(.+)"')
    title_pattern = re.compile('^#DRETITLE\s+(.+)')
    dbname_pattern = re.compile('^#DREDBNAME\s+(.+)')
    section_pattern = re.compile('^#DRESECTION\s+(.+)')
    date_pattern = re.compile('^#DREDATE\s+(.+)')
    content_pattern = re.compile('^#DRECONTENT')
    enddoc_pattern = re.compile('^#DREENDDOC')

    curr_doc = None
    in_content = False
    content = None
    iCount=0
    for line in sys.stdin:        
        m = enddoc_pattern.match(line)
        if m:
            # Finish
            curr_doc.content = content
            in_content = False
            content = ""
            print formatter.format(curr_doc),
            iCount+=1
            curr_doc = None
            continue
        if in_content:
            content = content + line
            continue
        m = reference_pattern.match(line)
        if m:
            curr_doc = IDX(m.group(1))
            continue
        m = field_pattern.match(line)
        if m:
            tmp = m.group(1)
            while (tmp in curr_doc.fields):
                tmp = tmp + '1'
            curr_doc.fields[tmp] = m.group(2)
            continue
        m = title_pattern.match(line)
        if m:
            curr_doc.title = m.group(1)
            continue
        m = dbname_pattern.match(line)
        if m:
            curr_doc.db = m.group(1)
            continue
        m = section_pattern.match(line)
        if m:
            curr_doc.section = m.group(1)
            continue
        m = date_pattern.match(line)
        if m:
            curr_doc.date = m.group(1)
            continue
        m = content_pattern.match(line)
        if m:
            in_content = True
            content = ""
            continue

if __name__ == '__main__':
    parseIDX()
