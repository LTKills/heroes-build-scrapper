import unicodedata
import requests
from bs4 import BeautifulSoup

class GetSoup:
  
  def get_soup(self, link):
      '''Gets a link, downloads page and gets soup
      Returns beautifulsoup object
      '''
      page = requests.get(link)
      return BeautifulSoup(page.content, 'html.parser')
