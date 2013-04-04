#!/usr/bin/python

import re
import codecs

class Document(object):
    def __init__(self,reference):
        self.reference = reference
        self.fields = dict([])
        self.title = None
        self.date = None
        self.section = None
        self.db = None
        self.content = None

    def write(self,fout):
        """
        Outputs a text representation of this Document to the fout.
        :param fout: An object that implements the write method.
        """
        fout.write(u'#DREREFERENCE {0}\n'.format(self.reference))
        if self.title:
            fout.write(u'#DRETITLE {0}\n'.format(self.title))
        if self.date:
            fout.write(u'#DREDATE {0}\n'.format(self.date))
        if self.section:
            fout.write(u'#DRESECTION {0}\n'.format(self.section))
        if self.db:
            fout.write(u'#DREDBNAME {0}\n'.format(self.reference))
        for key, value in self.fields.iteritems():
            fout.write(u'#DREFIELD {0}="{1}"\n'.format(key,value))
        if self.content:
            fout.write(u'#DRECONTENT\n{0}\n'.format(self.content))
        fout.write(u'#DREENDDOC\n\n')



def read_from_idx(filename,callback=None):
    """
    Reads each document from an IDX file and for each document calls the callback function with an
    instance of Document representing that entry.
    :param filename: Name of the IDX file to read.
    :param callback: A function that takes a single argument which is the reference to the Document object.
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

    with codecs.open(filename,'r','utf-8') as fin:
        curr_doc = None
        in_content = False
        content = None
        for line in fin:
            m = enddoc_pattern.match(line)
            if m:
                # Finish
                curr_doc.content = content
                in_content = False
                content = ""
                if callback:
                    callback(curr_doc)
                else:
                    results.append(curr_doc)
                curr_doc = None
                continue
            if in_content:
                content = content + line
                continue
            m = reference_pattern.match(line)
            if m:
                curr_doc = Document(m.group(1))
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
    return results

def project(idx_file_in, reference, filenameout):
    def reference_match(doc):
        if doc.reference == reference:
            with codecs.open(filenameout,'w','utf-8') as fout:
                doc.write(fout)
    
    read_from_idx(idx_file_in, reference_match)
    
def num_docs_in_idx(filename):
    """
    :param filename: name of IDX file.
    :returns: number of documents in the IDX file.
    """
    class DocumentCount(object):
        def __init__(self):
            self.count = 0
        def __call__(self,doc):
            self.count += 1

    doc_count = DocumentCount()
    read_from_idx(filename,doc_count)
    return doc_count.count
