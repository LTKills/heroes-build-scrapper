import unicodedata

class Normalize:      
  def normalize_hero_name(self, hero):
      '''Clears string so that fits link'''
      hero = unicodedata.normalize('NFD', hero).encode('ascii', 'ignore')
      hero = str(hero.decode('utf-8'))
      hero = hero.replace(' ', '-')
      hero = hero.replace('.', '')
      hero = hero.replace('\'', '')
      return hero.lower()

