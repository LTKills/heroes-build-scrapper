from heroes_build_scrapper.utils import normalize_hero_name


def test_normalize_name():
    raw_name = "Cab¶baGE P¥aTCH"
    norm_name = normalize_hero_name(raw_name)
    assert norm_name == "cabbage-patch"

