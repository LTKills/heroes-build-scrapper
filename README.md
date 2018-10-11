# heroes-build-scrapper

I've played Heroes of The Storm since its alpha releases but for some reason I've always found myself
digging builds in Icy Veins instead of comming up with my own. It was all flowers when I had two
monitors, but now that I'm back to single monitor I have to keep alt + tabbing whenever I have to
get a talent. Hopefully this project will help me by going to the page and telling me which talent
I need to get without leaving the game.

## files
This repo contains the following files
1. data.py
2. example.py
3. scrapping.py
4. single.py
5. utils.py
6. data
  a. heros.json
  b. levels.json

## Dependencies

Need to install these python packages

1. utils - pip install python-utils or easy_install python-utils or to download the latest version gpg –verify python-utils-    <version>.tar.gz.asc python-utils-<version>.tar.gz
2. import json or sudo apt install libpython2.7-stdlib and then import json
3. requests pip install requests or unless absolutely necessary easy_install requests
4. pip install beautifulsoup4 for the code "from bs4 import BeautifulSoup"
   That will install the latest BS4, which is 4.3.1 as of 2013-08-15. It supports Python 3.
5. import unicodedata
