import unicodedata
import json

class GetHeroes:  
  def get_heroes_list():
    with open('data/heroes.json', 'r') as fp:
      heroes = json.load(fp)
    
    return sorted(heroes)
      
      
    
