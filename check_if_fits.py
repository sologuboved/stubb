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
        title = chapter[TITLE]
        for ind in range(len(paragraphs)):
            paragraph = paragraphs[ind]
            length = len(paragraph)
            compare_and_shift(top, length, title, ind)

    prettyprint_top_output(top)
    return top


def compare_and_shift(top, length, chapter, paragraph):
    top_size = len(top)

    for bigger_ind in range(top_size):
        curr_length = top[bigger_ind][LENGTH]

        if curr_length == length:
            break

        if top[bigger_ind][LENGTH] < length:
            smaller_ind = top_size - 1

            while smaller_ind > bigger_ind:
                top[smaller_ind][LENGTH] = top[smaller_ind - 1][LENGTH]
                top[smaller_ind][CHAPTER] = top[smaller_ind - 1][CHAPTER]
                top[smaller_ind][PARAGRAPH] = top[smaller_ind - 1][PARAGRAPH]
                smaller_ind -= 1

            top[bigger_ind][LENGTH] = length
            top[bigger_ind][CHAPTER] = chapter
            top[bigger_ind][PARAGRAPH] = paragraph
            break


def prettyprint_top_output(top):
    for item in top:
        print("%s, paragraph %d, length: %d" % (item[CHAPTER], item[PARAGRAPH], item[LENGTH]))


if __name__ == '__main__':
    pass
    find_top(TOP)

