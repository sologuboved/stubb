import random
from json_operations import load_json

EXTRACTS = 'extracts/extracts.json'
TITLE = 'title'
TEXT = 'text'


def get_random_extract():
    extracts = load_json(EXTRACTS)
    random_ind = random.randrange(0, len(extracts))
    print("extract index:", random_ind, '\n')
    random_extract = extracts[random_ind]
    return random_extract[TITLE], random_extract[TEXT]

