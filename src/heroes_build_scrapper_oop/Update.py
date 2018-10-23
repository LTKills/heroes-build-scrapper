from Scrap import Scrap
from GetSoup import GetSoup
from Normalize import Normalize

import json
import requests
from bs4 import BeautifulSoup

class Update:
  def update_heroes_list(self):
      '''Automatically scrape the list of heroes from icy-veins and write it to a
      json file (heroes.json)
      '''
      heroes_names = set()
      roles = ['assassin', 'support', 'warrior', 'specialist']
  
      for role in roles:
          link = 'https://www.icy-veins.com/heroes/' + role + '-hero-guides'
          soupobj = GetSoup()
          soup = soupobj.get_soup(link)
  
          hero_block_tags = soup.find_all('div', class_='nav_content_block_entry_heroes_hero')
          for hero_block in hero_block_tags:
              hero = hero_block.find('span', class_='').contents[0]
              normalize = Normalize()
              name = normalize.normalize_hero_name(hero)
              heroes_names.add(name)
  
      with open('data/heroes.json', 'w') as fp:
          json.dump(list(heroes_names), fp)
  
  
  def update_all_builds(self):
      '''Updates all builds of all heroes (calls update_builds for all heroes)
      '''
      
      print('Starting full heroes build update')
  
      with open('data/heroes.json', 'r') as fp:
          heroes = json.load(fp)
  
      for hero in heroes:
        build = Scrap()        
        build.update_hero_builds(hero)
  
