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


def find_top():
    top = list()
    for ind in range(TOP):
        top.append({LENGTH: 0, CHAPTER: None, PARAGRAPH: None})

    for num in range(LAST_NUM + 1):
        chapter = load_json(MOBY_DICK_JSON_FOLDER + str(num) + JSON)
        paragraphs = chapter[TEXT]
        title = chapter[TITLE]
        for ind in range(len(paragraphs)):
            paragraph = paragraphs[ind]
            length = len(paragraph)
            compare_and_shift(top, length, ind, title)


def compare_and_shift(top, length, chapter, paragraph):
    for bigger_ind in range(TOP):
        if top[bigger_ind][LENGTH] < length:
            smaller_ind = TOP - 1
            # print(smaller_ind, bigger_ind)
            # print()
            while smaller_ind > bigger_ind:
                top[smaller_ind][LENGTH] = top[smaller_ind - 1][LENGTH]
                top[smaller_ind][CHAPTER] = top[smaller_ind - 1][CHAPTER]
                top[smaller_ind][PARAGRAPH] = top[smaller_ind - 1][PARAGRAPH]
                # print(top[smaller_ind])
                # print()
                smaller_ind -= 1
            top[bigger_ind][LENGTH] = length
            top[bigger_ind][CHAPTER] = chapter
            top[bigger_ind][PARAGRAPH] = paragraph
            break


if __name__ == '__main__':
    top1 = [{LENGTH: 10, CHAPTER: 0, PARAGRAPH: 0},
            {LENGTH: 7, CHAPTER: 1, PARAGRAPH: 1},
            {LENGTH: 5, CHAPTER: 2, PARAGRAPH: 2},
            {LENGTH: 3, CHAPTER: 3, PARAGRAPH: 3},
            {LENGTH: 1, CHAPTER: 4, PARAGRAPH: 4}]

    compare_and_shift(top1, 2, 5, 5)
    for t in top1:
        print(t)

