from heroes_build_scrapper.scrapping import get_builds_titles
from bs4 import BeautifulSoup
import pytest


@pytest.fixture()
def test_html():
    with open("src/tests/test_data/test_page.html", "rb") as f:
        raw_html = f.read()

    return raw_html


def test_retrieve_build_titles(test_html):
    test_soup = BeautifulSoup(test_html)
    retrieved_titles = get_builds_titles(test_soup.find_all('h3', class_='toc_no_parsing'))
    assert retrieved_titles == ['Chaos Reigns Build', 'Lightning Surge Build']
