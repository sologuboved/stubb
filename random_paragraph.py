import random
from json_operations import *

LAST_NUM = 136
MOBY_DICK_JSON_FOLDER = 'mobydick_json/'
MOBY_DICK_TXT_FOLDER = 'mobydick_txt/'
TITLES = 'titles.json'
JSON = '.json'
TXT = '.txt'
TITLE = 'title'
TEXT = 'text'


def get_chapter(num):
    try:
        return load_json(MOBY_DICK_JSON_FOLDER + str(num) + JSON)
    except FileNotFoundError:
        return


def get_paragraph(text, ind):
    try:
        return text[ind]
    except IndexError:
        return


def get_random_title_and_paragraph(last_num):
    random_num = random.randint(1, last_num)
    chapter = get_chapter(random_num)
    if chapter is None:
        return

    title = chapter[TITLE]
    text = chapter[TEXT]
    random_ind = random.randrange(0, len(text))
    print("paragraph index:", random_ind, '\n')
    paragraph = get_paragraph(text, random_ind)
    if paragraph is None:
        return

    return title, paragraph
