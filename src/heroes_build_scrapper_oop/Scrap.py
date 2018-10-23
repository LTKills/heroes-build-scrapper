from Normalize import Normalize
from GetSoup import GetSoup

import json
import os
from bs4 import BeautifulSoup

class Scrap:
  def get_hero_builds(self, hero):
    '''Scrape icy-veins for builds for the given hero.
    Returns two lists: one with other lists (each one for each build) and the
    second one with the builds' titles
    '''
    builds = []
    normalize = Normalize()
    hero = normalize.normalize_hero_name(hero)
    link = 'https://www.icy-veins.com/heroes/' + hero + '-build-guide'
    soupobj = GetSoup()
    soup = soupobj.get_soup(link)

    builds_tags = soup.find_all('div', class_='heroes_build_talents')
    build_title_tags = soup.find_all('h3', class_='toc_no_parsing')    
    build_titles = self.get_builds_titles(build_title_tags)

    for build_number, build_tag in enumerate(builds_tags):
        build = []
        talent_tiers = build_tag.find_all('span', class_= 'heroes_build_talent_tier_visual')

        # find out which block is painted with green (chosen talent)
        for tier in talent_tiers:
            children = tier.find_all('span')
            for j, child in enumerate(children):
                if('heroes_build_talent_tier_yes' in child['class']):
                    build.append(j+1)

        # append whole build to builds list
        builds.append(build[:])

    return builds, build_titles
  
  def get_builds_titles(self, build_title_tags):
    build_titles = []
    
    build_titles_aux = [title.get_text() for title in build_title_tags]
    
    # remove empty titles
    build_titles = [title for title in build_titles_aux if title != '']
    
    return build_titles
  def update_hero_builds(self, hero):
    '''Updates list of builds (in [hero name].json) for a given hero
    ''' 
    
    dump_list = []
    normalize = Normalize()
    hero = normalize.normalize_hero_name(hero)
    print('Updating builds for ' + hero + '...', end='')
    scrap = Scrap()
    builds, titles = scrap.get_hero_builds(hero)
    filename = 'data/builds/' + hero + '.json'

    for build, title in zip(builds, titles):
      dump_list.append(build)
      dump_list.append(title)

    with open(filename, 'w') as fp:
      json.dump(dump_list, fp)

    print('OK')

  def load_builds(self, hero):
    '''Loads builds for a hero'''
    hero = normalize_hero_name(hero)
    filename = 'data/builds/' + hero + '.json'
    load_list = []
    builds = []
    builds_titles = []

    # Scrape builds if not found locally
    if not os.path.exists(filename):
        print('Hero builds not found')
        self.update_hero_builds(hero)

    with open(filename, 'r') as fp:
        load_list = json.load(fp)

    for i in range(0, len(load_list) - 1, 2):
        builds.append(load_list[i])
        builds_titles.append(load_list[i + 1])

    print(builds, builds_titles)
    return builds, builds_titles
    
      
    

    
