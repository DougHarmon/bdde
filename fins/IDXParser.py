#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Mapper
# Purpose:
#
# Author:      Initial Version Created on MIT
#              04/05/2013 - Alan del Rio - Parse IDX from IDOL
#
# Copyright:   (c) Hewlett Packard
#-------------------------------------------------------------------------------
import sys
import re

class IDX(object):
    def __init__(self,reference):
        self.reference = reference
        self.fields = dict()
        self.desc = dict([])

class IDXParser:
    def __init__(self,objFormatter,objWritter):
        self.__objFormatter=objFormatter
        self.__objWritter=objWritter
    def parseIDX(self,lines):
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
        content = ""
        iCount=0
        for line in lines:
            #line=line.encode('UTF-8')
            m = enddoc_pattern.match(line)
            if m:
                # Finish
                curr_doc.desc['DRECONTENT']  = content
                in_content = False
                content = ""
                self.__objWritter.write(self.__objFormatter.format(curr_doc))
                iCount+=1
                curr_doc = None
                continue
            if in_content:
                content = content + line
                continue
            m = reference_pattern.match(line)
            if m:
                curr_doc = IDX(m.group(1))
                curr_doc.desc['DREREFERENCE']=m.group(1)
                continue
            m = field_pattern.match(line)
            if m:
                if m.group(1) in curr_doc.fields:
                    curr_doc.fields[m.group(1)].append(m.group(2))
                else:
                    curr_doc.fields[m.group(1)]=[m.group(2)]
                continue
            m = title_pattern.match(line)
            if m:
                curr_doc.desc['DRETITLE'] = m.group(1)
                continue
            m = dbname_pattern.match(line)
            if m:
                curr_doc.desc['DREDBNAME'] = m.group(1)
                continue
            m = section_pattern.match(line)
            if m:
                curr_doc.desc['DRESECTION'] = m.group(1)
                continue
            m = date_pattern.match(line)
            if m:
                curr_doc.desc['DREDATE'] = m.group(1)
                continue
            m = content_pattern.match(line)
            if m:
                in_content = True
                content=""
                continue