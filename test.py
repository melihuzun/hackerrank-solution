from total_goals_by_team import scrape_pages, get_data, get_goals
import pytest


def test_types():
    ou_list = []
    assert type(scrape_pages(2011, 1, ou_list)) == int
    assert type(get_data(2011)) == int
    assert type(get_goals(2011)) == int


def test_years():
    assert get_goals(2011) == 516
    assert get_goals(2012) == 501
    assert get_goals(2010) == 0
