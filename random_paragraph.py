import random
from json_operations import *

EXTENSION = '.json'
FOLDERNAME = 'mobydick_json/'
TITLE = 'title'
TEXT = 'text'
LAST_NUM = 136


def get_chapter(num):
    try:
        return load_json(FOLDERNAME + str(num) + EXTENSION)
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
