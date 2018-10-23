import unicodedata
import requests
import json

class Print:
  def __init__(self, hero, build, title):
    self.hero = hero
    self.build = build
    self.title = title

    def prinnnt_build(self, build, title):
      string = ''

      with open('data/levels.json', 'r') as fp:
        levels = json.load(fp)
  
      string += title + '\n'
      for level, talent in zip(levels, build):
        string += 'Level ' + str(level) + ' Talent ' + str(talent) + '\n'
        
      return string

    def print_hero_builds(self, hero):
        string = ''
    
        string += '-------------------------------- ' + hero + ' --------------------------------' + '\n'
        builds, titles = load_builds(hero)
        for build, title in zip(builds, titles):
            string += print_build(build, title)
            string += '\n'
    
    return string


    def print_all_builds():
        heroes = get_heroes_list()
    
        for hero in heroes:
          print_hero_builds(hero)

          
