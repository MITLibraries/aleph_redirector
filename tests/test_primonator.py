from redirector.primonator import permalink_to_id, aleph_id_to_alma_id, alma_id_to_link


def test_permalink_to_id():
    assert permalink_to_id(None) is None
    assert permalink_to_id(
        'http://library.mit.edu/item/000192838') == '000192838'
    assert permalink_to_id(
        'http://library.mit.edu/item/000801611') == '000801611'
    assert permalink_to_id(
        'http://library.mit.edu/item/000826493') == '000826493'
    assert permalink_to_id(
        'http://library.mit.edu/item/000041611') == '000041611'


def test_aleph_id_to_alma_id():
    assert aleph_id_to_alma_id(None) is None
    assert aleph_id_to_alma_id('000192838') == 'alma990001928380106761'
    assert aleph_id_to_alma_id('000801611') == 'alma990008016110106761'


def test_alma_id_to_link():
    url = 'https://example.com/hallo/'
    assert alma_id_to_link(None, url) is None
    assert alma_id_to_link('alma990001928380106761',
                           url) == 'https://example.com/hallo/alma990001928380106761'
    assert alma_id_to_link('alma990008016110106761',
                           url) == 'https://example.com/hallo/alma990008016110106761'
