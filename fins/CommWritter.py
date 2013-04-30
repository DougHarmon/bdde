import sys
import codecs
def CSV():
    with codecs.open("csv_data.csv", 'a') as fout:
        for line in sys.stdin:
            fout.write(line)

if __name__ == '__main__':
    CSV()