import requests
from bs4 import BeautifulSoup
from process_input_and_output import *
from substitutes import *

EXTRACTS_URL = 'http://www.powermobydick.com/Moby0001.html'
EXTRACTS_FOLDER = 'extracts/'
EXTRACTS = 'extracts'
RAW_EXTRACTS = 'raw_extracts'
JSON = '.json'
TXT = '.txt'
TEXT = 'text'
TITLE = 'title'


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
    filename = EXTRACTS_FOLDER + RAW_EXTRACTS + JSON
    print("Dumping raw extracts to %s...\n" % filename)
    raw_extracts = scrape_extracts()
    dump_json(raw_extracts, filename)


def replace_raw_extract(ind, substitute):
    filename = EXTRACTS_FOLDER + RAW_EXTRACTS + JSON
    raw_extracts = load_json(filename)
    raw_extracts[ind] = substitute
    dump_json(raw_extracts, filename)


def merge_raw_extracts(start_ind, end_ind):
    filename = EXTRACTS_FOLDER + RAW_EXTRACTS + JSON
    raw_extracts = load_json(filename)
    to_merge = raw_extracts[start_ind: end_ind + 1]

    merged = str()
    for raw_extract in to_merge:
        merged += '\n' + raw_extract

    res = raw_extracts[: start_ind] + [merged] + raw_extracts[end_ind + 1:]

    dump_json(res, filename)


def omit_raw_extract(ind):
    filename = EXTRACTS_FOLDER + RAW_EXTRACTS + JSON
    raw_extracts = load_json(filename)
    dump_json(raw_extracts[: ind] + raw_extracts[ind + 1:], filename)


def cook_extracts():
    # Separate extracts from sources with the help of dictinaries {'text': text, 'title': title}
    # and dump them into a new .json
    extracts = list()
    raw_extracts = load_json(EXTRACTS_FOLDER + RAW_EXTRACTS + JSON)
    ind = 0
    for raw_extract in raw_extracts:
        print(ind)
        ind += 1
        extract, source = reprocess_extract(raw_extract)
        extracts.append({TEXT: extract, TITLE: source})
    dump_json(extracts, EXTRACTS_FOLDER + EXTRACTS + JSON)


def reprocess_extract(raw_extract):
    raw_extract = raw_extract[1:]
    ind = 0
    while raw_extract[ind] != '"':
        ind += 1
    extract = raw_extract[: ind]
    source = raw_extract[ind + 1:].strip()
    # print(extract)
    # print()
    # print(source)
    return extract, source


def json_to_txt():
    extracts = load_json(EXTRACTS_FOLDER + EXTRACTS + JSON)
    ind = 0
    with open(EXTRACTS_FOLDER + EXTRACTS + TXT, 'w') as handler:
        for extract in extracts:
            handler.write("<%d>\n" % ind)
            handler.write(extract[TEXT] + '\n\n')
            handler.write("(%s)\n\n\n" % extract[TITLE])
            ind += 1


def prettyprint_raw_extracts():
    raw_extracts = load_json(EXTRACTS_FOLDER + RAW_EXTRACTS + JSON)
    ind = 0
    for raw_extract in raw_extracts:
        print(ind)
        print(raw_extract)
        print()
        ind += 1

