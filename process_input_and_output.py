from random_paragraph import *
from random_extract import *
from check_if_fits import elicit_paragraph

INVALID_INPUT = "Invalid input!"
WRONG = "Something went wrong!"
TOO_MUCH = 'There are as many as 136 Chapters in "Moby Dick", including the Epilogue'
NOT_ZERO_ETC = 'The first chapter is chapter 1, named "Loomings"'
NO_PARAGRAPH = "No such paragraph; the last in this chapter has index "


def process_input_for_cet(user_input):
    if not user_input:
        try:
            title, paragraph = get_random_title_and_paragraph(last_num=LAST_NUM)
            return process_output(title, paragraph)
        except TypeError:
            return WRONG

    try:
        last_num = int(user_input)
    except ValueError:
        return INVALID_INPUT

    if last_num > LAST_NUM:
        return TOO_MUCH

    if last_num < 1:
        return NOT_ZERO_ETC

    try:
        title, paragraph = get_random_title_and_paragraph(last_num=last_num)
    except TypeError:
        return WRONG

    return process_output(title, paragraph)


def process_input_for_lib():
    return process_output(*get_random_extract())


def process_input_for_lev(chapter_num, paragraph_ind):
    try:
        chapter_num = int(chapter_num.strip())
        paragraph_ind = int(paragraph_ind.strip())
    except ValueError:
        return INVALID_INPUT
    if chapter_num == 0:
        return NOT_ZERO_ETC
    if chapter_num > LAST_NUM:
        return TOO_MUCH
    paragraph = elicit_paragraph(chapter_num, paragraph_ind)
    if type(paragraph) is int:
        return NO_PARAGRAPH + str(paragraph - 1)
    if not paragraph:
        return WRONG
    return process_output(*paragraph)


def process_output(title, text):
    return "%s\n\n(%s)" % (text, title)

