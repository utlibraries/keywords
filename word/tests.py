import pytest
from .populate import Populator


@pytest.fixture
def urls():
    return {
        "data": {'topic': 'bob', 'concepts': [{'concept': 'poppy', 'keyconcepts': ['spawn', 'egg', 'tournment']},
                                              {'concept': 'clouds', 'keyconcepts': ['black', 'soul', 'death']}],
                'max_words': 2},
       "catalog": 'https://search.lib.utexas.edu/discovery/search?query=any,contains,(poppy+OR+spawn+OR+egg+OR+tournment)+AND+(clouds+OR+black+OR+soul+OR+death)&tab=Everything&search_scope=MyInst_and_CI&vid=01UTAU_INST:SEARCH&lang=en&offset=0',
       "academic": 'http://web.a.ebscohost.com/ehost/resultsadvanced?vid=1&bdata=JmRiPWE5aCZ0eXBlPTEmc2l0ZT1laG9zdC1saXZl&bquery=(poppy+OR+spawn+OR+egg+OR+tournment)+AND+(clouds+OR+black+OR+soul+OR+death)',
       "jstor":  'https://www.jstor.org/action/doBasicSearch?Query=(poppy+OR+spawn+OR+egg+OR+tournment)+AND+(clouds+OR+black+OR+soul+OR+death)'}


def test_populator_catalog(urls):
    my_urls = Populator.create_query(urls['data'])
    assert urls['catalog'] == my_urls['catalog']


def test_populator_jstor(urls):
    my_urls = Populator.create_query(urls['data'])
    assert urls['jstor'] == my_urls['jstor']


def test_populator_academic(urls):
    my_urls = Populator.create_query(urls['data'])
    assert urls['academic'] == my_urls['academic']