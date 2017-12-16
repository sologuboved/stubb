from random_paragraph import *

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
        return process_output(title, paragraph)
    except TypeError:
        return WRONG


def process_output(title, paragraph):
    return "%s\n\n(%s)" % (paragraph, title)


if __name__ == '__main__':
    pass
    # random.seed(19)
    # c = process_input_for_cet('75')
    # print(c)
