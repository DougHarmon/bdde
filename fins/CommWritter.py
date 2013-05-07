import sys
import codecs
def CSV():
    with codecs.open("csv_data.csv", 'a') as fout:
        for line in sys.stdin:
            fout.write(line)

def CSVFile():
    sFilter=""
    for line in sys.stdin:
        if line.replace("\n","")!="":
            arrLine=line.split("~",1)
            if sFilter=="":
                sFilter=arrLine[0]
                fout=codecs.open(sFilter, 'a')

            if  sFilter==arrLine[0]:
                    fout.write(arrLine[1])
            else:
                print line

if __name__ == '__main__':
    CSVFile()