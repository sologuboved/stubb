def get_titles():
    titles = list()
    odd = True
    with open('titles.txt') as handler:
        raw_titles = handler.readlines()
        for raw_title in raw_titles:
            if odd:
                titles.append(raw_title.strip())
            else:
                pass
            odd = not odd
    return titles
