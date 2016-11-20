import os
import re
import unicodedata
from makeuplink import get_sentiment

DATAPATH = 'youtubeScraper/ok/'


def normalize(value):
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    value = unicode(re.sub('[-\s]+', '-', value))
    return value


def passfile(filename):
    newfilename = normalize(filename)
    os.rename(DATAPATH+filename, DATAPATH+newfilename)


def index_lyrics(filename, score):
    with open('INDEX.db', 'a') as mainindex:
        mainindex.writelines(str(score) + ' ' + filename + '\n')

if __name__ == '__main__':
    td = os.listdir(DATAPATH)
    for d in td:
        passfile(d)
        index_lyrics(d, get_sentiment(DATAPATH+d))
