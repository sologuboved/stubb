import random
from json_operations import *

LAST_NUM = 136
MOBY_DICK_JSON_FOLDER = 'mobydick_json/'
EXTENSION = '.json'
TITLE = 'title'
TEXT = 'text'


def get_chapter(num):
    try:
        return load_json(MOBY_DICK_JSON_FOLDER + str(num) + EXTENSION)
    except FileNotFoundError:
        return


def get_paragraph(text, ind):
    try:
        return text[ind]
    except IndexError:
        return


def get_random_title_and_paragraph(last_num):
    num = random.randint(1, last_num)
    chapter = get_chapter(num)
    if chapter is None:
        return

    title = chapter[TITLE]
    text = chapter[TEXT]
    ind = random.randrange(0, len(text))
    print("paragraph index:", ind, '\n')
    paragraph = get_paragraph(text, ind)
    if paragraph is None:
        return

    return title, paragraph
