# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def scrape():
    m_d = list()
    chapter_urls = generate_chapter_urls()
    for chapter_url in chapter_urls:
        title, text = scrape_chapter(chapter_url)
        chapter = {'title': title, 'text': text}
        m_d.append(chapter)
    epilogue_title, epilogue_text = get_epilogue()
    m_d.append({'title': epilogue_title, 'text': epilogue_text})
    return m_d


def generate_chapter_urls():
    print("Generating chapter urls...")
    prefix = 'http://www.mobydickthewhale.com/moby-dick/moby-dick-chapter-'
    postfix = '.htm'
    return [prefix + str(num) + postfix for num in range(1, 136)]


def scrape_chapter(chapter_url):
    print("Scraping", chapter_url + '...')
    chapter_html = requests.get(chapter_url).content
    soup = BeautifulSoup(chapter_html, 'html.parser')
    title = soup.find('title').text
    paragraphs = [paragraph.text for paragraph in soup.find_all('p')[: -2]]
    return title, paragraphs


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


if __name__ == '__main__':
    pass
    # t, parags = scrape_chapter('http://www.mobydickthewhale.com/moby-dick/moby-dick-epilogue.htm')
    # print(t)
    # print()
    # for p in parags:
    #     print(p)
    # print()

    # print(generate_chapter_urls())
    # print()

    # print(get_epilogue())
    # print()

    s = scrape()
    for ch in s:
        print()
        print(ch['title'])
        print()
        for p in ch['text']:
            print(p)
            print()


