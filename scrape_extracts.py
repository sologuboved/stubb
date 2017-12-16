import requests
from bs4 import BeautifulSoup
from json_operations import *

TEXT = 'text'
SOURCE = 'source'
FOLDER = 'extracts/'
FILENAME = 'extracts'
FILENAME_RAW = 'raw_extracts'
JSON = '.json'
TXT = '.txt'
EXTRACTS_URL = 'http://www.powermobydick.com/Moby0001.html'


def scrape_and_dump():
    pass


def scrape_extracts():
    print('Scraping extracts...\n')
    extracts = list()
    soup = BeautifulSoup(requests.get(EXTRACTS_URL).content, 'html.parser')
    raw_extracts = soup.find_all('p')[28: -1]
    for raw_extract in raw_extracts:
        raw_extract = raw_extract.text.strip()
        if not raw_extract.startswith('page'):
            extracts.append(raw_extract)
    return extracts


def dump_raw_extracts():
    filename = FOLDER + FILENAME_RAW + JSON
    print("Dumping raw extracts to %s...\n" % filename)
    raw_extracts = scrape_extracts()
    dump_json(raw_extracts, filename)


if __name__ == '__main__':
    pass
    r_e = load_json(FOLDER + FILENAME_RAW + JSON)
    for e in r_e:
        print(e)
        print()


