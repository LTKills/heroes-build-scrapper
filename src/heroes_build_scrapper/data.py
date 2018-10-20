'''Gets all builds for all heroes
(prints or writes to file (json?) -> JSON!
'''
from .utils import get_soup, normalize_hero_name
from .scrapping import get_hero_builds
import json
import requests
from bs4 import BeautifulSoup


def update_heroes_list():
    '''Automatically scrape the list of heroes from icy-veins and write it to a
    json file (heroes.json)
    '''
    heroes_names = set()
    roles = ['assassin', 'support', 'warrior', 'specialist']

    for role in roles:
        link = 'https://www.icy-veins.com/heroes/' + role + '-hero-guides'
        soup = get_soup(link)

        hero_block_tags = soup.find_all('div', class_='nav_content_block_entry_heroes_hero')
        for hero_block in hero_block_tags:
            name = normalize_hero_name(hero_block.find('span', class_='').contents[0])
            heroes_names.add(name)

    with open('data/heroes.json', 'w') as fp:
        json.dump(list(heroes_names), fp)


def update_hero_builds(hero):
    '''Updates list of builds (in [hero name].json) for a given hero
    '''
    dump_list = []
    hero = normalize_hero_name(hero)
    print('Updating builds for ' + hero + '...', end='')
    builds, titles = get_hero_builds(hero)
    filename = 'data/builds/' + hero + '.json'

    for build, title in zip(builds, titles):
        dump_list.append(build)
        dump_list.append(title)

    with open(filename, 'w') as fp:
        json.dump(dump_list, fp)

    print('OK')


def update_all_builds():
    '''Updates all builds of all heroes (calls update_builds for all heroes)
    '''
    print('Starting full heroes build update')

    with open('data/heroes.json', 'r') as fp:
        heroes = json.load(fp)

    for hero in heroes:
        update_hero_builds(hero)



