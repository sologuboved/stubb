# -*- coding: utf-8 -*-

import json
import requests
from bs4 import BeautifulSoup

FOLDERNAME = "Moby Dick/"
TITLE = 'title'
TEXT = 'text'
TITLES = 'titles.json'


def generate_filename(ind):
    return FOLDERNAME + str(ind) + '.json'


def dump_json(data, json_filename):
    with open(json_filename, 'w') as handler:
        json.dump(data, handler)


def load_json(json_filename):
    with open(json_filename) as data:
        return json.load(data)


def scrape_and_dump_novel():
    print('Scraping "Moby Dick...\n')
    titles = load_json(TITLES)
    ind = 1
    for title in titles:
        chapter_url = generate_chapter_url(title)
        text = scrape_chapter(chapter_url, ind)
        chapter = {TITLE: title, TEXT: text}
        filename = generate_filename(ind)
        print("Dumping %s to %s" % (title, filename))
        dump_json(chapter, filename)
        ind += 1
    epilogue_title, epilogue_text = get_epilogue()
    epilogue = {TITLE: epilogue_title, TEXT: epilogue_text}
    filename = generate_filename(ind)
    print("Dumping %s to %s" % (epilogue_title, filename))
    dump_json(epilogue, filename)


# def generate_chapter_urls():
    # titles = get_titles()
    # return [generate_chapter_url(title) for title in get_titles()]
    # for title in titles:
    #     chapter_url = generate_chapter_url(title)
    #     html = requests.get(chapter_url).content
    #     soup = BeautifulSoup(html, 'html.parser')
    #     if "The page you requested could not be found" in str(soup):
    #         print(chapter_url, '!!!!!!!!!')


def generate_chapter_url(title):
    prefix = 'https://americanliterature.com/author/herman-melville/book/moby-dick-or-the-whale/'
    ch_num, *ch_head = map(lambda i: i.strip(), title.split('-'))
    ch_num = list(map(lambda i: i.lower(), ch_num.split()))
    postfix = '-'.join(ch_num + [''.join(filter(str.isalpha, word)) for word in " ".join(ch_head).lower().split()])
    return prefix + postfix


def scrape_chapter(chapter_url, ind):
    print("Scraping chapter", ind)
    html = requests.get(chapter_url).content
    soup = BeautifulSoup(html, 'html.parser')
    paragraphs = soup.find_all('p')
    print(paragraphs)

    return paragraphs


# def scrape_titles():
#     print("Scraping titles...")
#     titles = list()
#     html = requests.get('http://www.mobydickthewhale.com/moby-dick/moby-dick-table-of-contents.htm').content
#     raw_titles = BeautifulSoup(html, 'html.parser').find_all('a', href=True)[3: -9]
#     ind = 0
#     while ind + 1 < len(raw_titles):
#         titles.append(raw_titles[ind].text + ": " + raw_titles[ind + 1].text)
#         ind += 2
#     return titles


def get_epilogue():
    print("Obtaining epilogue...")
    title = 'Moby-Dick Epilogue'
    paragraph0 = '"and I only am escaped alone to tell thee." Job'
    paragraph1 = "The drama's Done. Why then here does any one step forth? - Because one did survive the wreck."
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


def prettyprint_chapter(ind):
    chapter = load_json(FOLDERNAME + str(ind) + '.json')
    print(chapter[TITLE])
    print()
    print(chapter[TEXT][3])
    for paragraph in chapter[TEXT]:
        print(paragraph)
        print()
    print()


if __name__ == '__main__':
    pass

    # for i in generate_chapter_ids():
    #     print(i)

    # for t in scrape_titles():
    #     print(t)

    # print(generate_chapter_url("Chapter 103: Measurement of The Whale's Skeleton"))

    # print(generate_chapter_urls())

    # dump_titles(get_titles())

    # titles = load_json('titles.json')
    # for t in titles:
    #     print(t)

    # ts = get_titles(TITLES)
    # for t in ts:
    #     print(t)

