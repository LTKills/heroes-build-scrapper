'''Gets all builds for all heroes
(prints or writes to file (json?) -> JSON!
'''
import json
from .scrapping import update_hero_builds
from .utils import get_soup, normalize_name


def update_heroes_list():
    '''Automatically scrape the list of heroes from icy-veins and write it to a
    json file (heroes.json)
    '''
    heroes_names = set()
    roles = ['assassin', 'support', 'warrior', 'specialist']

    for role in roles:
        link = 'https://www.icy-veins.com/heroes/' + role + '-hero-guides'
        soup = get_soup(link)

        block_tags = soup.find_all(
            'div',
            class_='nav_content_block_entry_heroes_hero'
        )
        for block in block_tags:
            name = normalize_name(block.find('span', class_='').contents[0])
            heroes_names.add(name)

    with open('data/heroes.json', 'w') as fp:
        json.dump(list(heroes_names), fp)


def update_all_builds():
    '''Updates all builds of all heroes (calls update_builds for all heroes)
    '''
    print('Starting full heroes build update')

    with open('data/heroes.json', 'r') as fp:
        heroes = json.load(fp)

    for hero in heroes:
        update_hero_builds(hero)
