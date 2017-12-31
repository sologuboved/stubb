# Chapter 31, paragraph 1, length: 3668
# Chapter 99, paragraph 8, length: 3637
# Chapter 35, paragraph 5, length: 3518
# Chapter 27, paragraph 8, length: 2955
# Chapter 54, paragraph 8, length: 2929

from json_operations import load_json

LAST_NUM = 136
TOP = 5
MOBY_DICK_JSON_FOLDER = 'mobydick_json/'
JSON = '.json'
TITLE = 'title'
TEXT = 'text'
LENGTH = 'length'
CHAPTER = 'chapter'
PARAGRAPH = 'paragraph'


def generate_top_dummy(top_size):
    top = list()
    for ind in range(top_size):
        top.append({LENGTH: 0, CHAPTER: None, PARAGRAPH: None})
    return top


def find_top(top_size):
    top = generate_top_dummy(top_size)

    for num in range(1, LAST_NUM + 1):
        chapter = load_json(MOBY_DICK_JSON_FOLDER + str(num) + JSON)
        paragraphs = chapter[TEXT]
        for ind in range(len(paragraphs)):
            paragraph = paragraphs[ind]
            length = len(paragraph)
            update_top(top, length, num, ind)

    prettyprint_top_output(top)
    return top


def update_top(top, length, chapter, paragraph):
    for item in top:
        if item[LENGTH] == length:
            return
    top.append({LENGTH: length, CHAPTER: chapter, PARAGRAPH: paragraph})
    top.sort(key=lambda i: i[LENGTH], reverse=True)
    del top[-1]


def prettyprint_top_output(top):
    for item in top:
        print("Chapter %d, paragraph %d, length: %d" % (item[CHAPTER], item[PARAGRAPH], item[LENGTH]))


def elicit_paragraph(chapter_num, paragraph_ind):
    try:
        chapter = load_json(MOBY_DICK_JSON_FOLDER + str(chapter_num) + JSON)
    except FileNotFoundError:
        return None
    title = chapter[TITLE]
    paragraphs = chapter[TEXT]
    try:
        return title, paragraphs[paragraph_ind]
    except IndexError:
        return len(paragraphs)

