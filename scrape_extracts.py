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


def replace_raw_extract(ind, substitute):
    filename = FOLDER + FILENAME_RAW + JSON
    raw_extracts = load_json(filename)
    raw_extracts[ind] = substitute
    dump_json(raw_extracts, filename)


def merge_raw_extracts(start_ind, end_ind):
    filename = FOLDER + FILENAME_RAW + JSON
    raw_extracts = load_json(filename)
    to_merge = raw_extracts[start_ind: end_ind + 1]

    merged = str()
    for raw_extract in to_merge:
        merged += '\n' + raw_extract

    res = raw_extracts[: start_ind] + [merged] + raw_extracts[end_ind + 1:]

    dump_json(res, filename)


def omit_raw_extract(ind):
    filename = FOLDER + FILENAME_RAW + JSON
    raw_extracts = load_json(filename)
    dump_json(raw_extracts[: ind] + raw_extracts[ind + 1:], filename)


def prettyprint_raw_extracts():
    raw_extracts = load_json(FOLDER + FILENAME_RAW + JSON)
    ind = 0
    for raw_extract in raw_extracts:
        print(ind)
        print(raw_extract)
        print()
        ind += 1


if __name__ == '__main__':
    pass

    # omit_raw_extract(46)
    # merge_raw_extracts(69, 70)

    # replace_raw_extract(51, s51)

    # print(s60)

    prettyprint_raw_extracts()





