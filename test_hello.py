from hello import add


def test_add():
    assert 2 == add(1, 1)

from wikibot import scrape

def test_scrape():
    assert "Microsoft" in scrape("Microsoft")