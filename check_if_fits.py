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
            compare_and_shift(top, TOP, length, ind, title)
    return top


def compare_and_shift(top, length, chapter, paragraph):
    top_size = len(top)
    for bigger_ind in range(top_size):
        curr_length = top[bigger_ind][LENGTH]
        if curr_length == length:
            break
        if top[bigger_ind][LENGTH] < length:
            smaller_ind = top_size - 1
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
    # top1 = [{LENGTH: 10, CHAPTER: 0, PARAGRAPH: 0},
    #         {LENGTH: 7, CHAPTER: 1, PARAGRAPH: 1},
    #         {LENGTH: 5, CHAPTER: 2, PARAGRAPH: 2},
    #         {LENGTH: 3, CHAPTER: 3, PARAGRAPH: 3},
    #         {LENGTH: 1, CHAPTER: 4, PARAGRAPH: 4}]
    #
    # compare_and_shift(top1, 2, 5, 5)
    # for t in top1:
    #     print(t)

    top2 = [{LENGTH: 0, CHAPTER: None, PARAGRAPH: None},
            {LENGTH: 0, CHAPTER: None, PARAGRAPH: None},
            {LENGTH: 0, CHAPTER: None, PARAGRAPH: None},
            {LENGTH: 0, CHAPTER: None, PARAGRAPH: None},
            {LENGTH: 0, CHAPTER: None, PARAGRAPH: None}]

    compare_and_shift(top2, 1, 1, 1)
    compare_and_shift(top2, 30, 30, 30)
    compare_and_shift(top2, 10, 10, 10)
    compare_and_shift(top2, 3, 3, 3)
    compare_and_shift(top2, 50, 50, 50)
    compare_and_shift(top2, 20, 20, 20)
    compare_and_shift(top2, 15, 15, 15)
    compare_and_shift(top2, 50, 50, 50)
    compare_and_shift(top2, 100, 100, 100)
    compare_and_shift(top2, 40, 40, 40)
    compare_and_shift(top2, 70, 70, 70)

    for t in top2:
        print(t)

