import random
from basic_operations import load_json
from global_vars import *


def get_random_extract():
    extracts = load_json(EXTRACTS)
    random_ind = random.randrange(0, len(extracts))
    print("extract index:", random_ind, '\n')
    random_extract = extracts[random_ind]
    return random_extract[TITLE], random_extract[TEXT]

