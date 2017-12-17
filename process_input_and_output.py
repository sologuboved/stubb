from random_paragraph import *
from random_extract import *

INVALID_INPUT = "Invalid input!"
WRONG = "Something went wrong!"
TOO_MUCH = 'There are as many as 136 Chapters in "Moby Dick", including the Epilogue'
NOT_ZERO_ETC = 'The first chapter is chapter 1, named "Loomings"'


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


def process_output(title, text):
    return "%s\n\n(%s)" % (text, title)


if __name__ == '__main__':
    print(process_input_for_cet(None))
