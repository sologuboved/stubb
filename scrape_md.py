# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from json_operations import *

MOBY_DICK_JSON_FOLDER = 'mobydick_json/'
MOBY_DICK_TXT_FOLDER = 'mobydick_txt/'
TITLES = 'titles.json'
JSON = '.json'
TXT = '.txt'
TITLE = 'title'
TEXT = 'text'


def generate_filename(ind, foldername, extension):
    return foldername + str(ind) + extension


def scrape_and_dump_novel(txt):
    print('Scraping "Moby Dick"...\n')
    titles = load_json(TITLES)
    ind = 1
    for title in titles:
        chapter_url = generate_chapter_url(title)
        text = scrape_chapter(chapter_url, ind)
        chapter = {TITLE: title, TEXT: text}
        dump_chapter_to_json(ind, title, chapter)
        if txt:
            dump_chapter_to_txt(ind, title, text)
        ind += 1
    epilogue_title, epilogue_text = get_epilogue()
    epilogue = {TITLE: epilogue_title, TEXT: epilogue_text}
    dump_chapter_to_json(ind, epilogue_title, epilogue)
    if txt:
        dump_chapter_to_txt(ind, epilogue_title, epilogue_text)


def dump_chapter_to_json(ind, title, chapter):
    json_filename = generate_filename(ind, MOBY_DICK_JSON_FOLDER, JSON)
    print("Dumping %s to %s" % (title, json_filename))
    dump_json(chapter, json_filename)


def dump_chapter_to_txt(ind, title, chapter):
    txt_filename = generate_filename(ind, MOBY_DICK_TXT_FOLDER, TXT)
    print("Dumping %s to %s" % (title, txt_filename))
    with open(txt_filename, 'w') as handler:
        handler.write(title + '\n\n')
        for paragraph in chapter:
            handler.write(paragraph + '\n')


def generate_chapter_url(title):
    prefix = 'https://americanliterature.com/author/herman-melville/book/moby-dick-or-the-whale/'
    ch_num, *ch_head = map(lambda i: i.strip(), title.split('-'))
    ch_num = list(map(lambda i: i.lower(), ch_num.split()))
    postfix = '-'.join(ch_num + [''.join(filter(str.isalpha, word)) for word in " ".join(ch_head).lower().split()])
    return prefix + postfix


def scrape_chapter(chapter_url, ind):
    print("Scraping chapter", ind)
    soup = BeautifulSoup(requests.get(chapter_url).content, 'html.parser')
    return [paragraph.text for paragraph in soup.find_all('p')[: -2] if paragraph.text]


def get_epilogue():
    print("Obtaining epilogue...")
    title = 'Moby-Dick Epilogue'
    paragraph0 = '"and I only am escaped alone to tell thee" Job'
    paragraph1 = "The drama's done. Why then here does any one step forth? - Because one did survive the wreck."
    paragraph2 = "It so chanced, that after the Parsee's disappearance, I was he whom the Fates ordained to take the " \
                 "place of Ahab's bowsman, when that bowsman assumed the vacant post; the same, who, when on the " \
                 "last day the three men were tossed from out the rocking boat, was dropped astern. So. floating on " \
                 "the margin of the ensuing scene, and in full sight of it, when the half-spent suction of the sunk " \
                 "ship reached me, I was then, but slowly, drawn towards the closing vortex. When I reached it, it " \
                 "had subsided to a creamy pool. Round and round, then, and ever contracting towards the button-like " \
                 "black bubble at the axis of that slowly wheeling circle, like another ixion I did revolve. till " \
                 "gaining that vital centre, the black bubble upward burst; and now, liberated by reason of its " \
                 "cunning spring, and owing to its great buoyancy, rising with great force, the coffin like-buoy " \
                 "shot lengthwise from the sea, fell over, and floated by my side. Buoyed up by that coffin, for " \
                 "almost one whole day and night, I floated on a soft and dirge-like main. The unharming sharks, " \
                 "they glided by as if with padlocks on their mouths; the savage sea-hawks sailed with sheathed " \
                 "beaks. On the second day, a sail drew near, nearer, and picked me up at last. It was the " \
                 "devious-cruising Rachel, that in her retracing search after her missing children, only found " \
                 "another orphan."
    return title, [paragraph0, paragraph1, paragraph2]


def prettyprint_chapter_from_json(ind):
    chapter = load_json(MOBY_DICK_JSON_FOLDER + str(ind) + '.json')
    print(chapter[TITLE])
    print()
    for paragraph in chapter[TEXT]:
        print(paragraph)
        print()
    print()
