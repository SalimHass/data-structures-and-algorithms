import pytest
from data_structures_and_algorithms.hashtable import Hashtable

def test_contains1(hashtable):
    actual = hashtable.contains("julia")
    expected = True
    assert actual == expected 

def test_contains2(hashtable):
    actual = hashtable.contains("uljia")
    expected = True
    assert actual == expected 

def test_contains3(hashtable):
    actual = hashtable.contains("salim")
    expected = True
    assert actual == expected 

def test_contains4(hashtable):
    actual = hashtable.contains("salmi")
    expected = False
    assert actual == expected 

def test_contains5(hashtable):
    actual = hashtable.contains("juila")
    expected = False
    assert actual == expected     

def test_contains6(hashtable):
    actual = hashtable.contains("tom")
    expected = False
    assert actual == expected

def test_keys(hashtable):
    actual = hashtable.keys()
    expected = ['julia', 'uljia', 'salim']
    assert actual == expected


def test_get1(hashtable):
    actual = hashtable.get("julia")
    expected = "Has"
    assert actual == expected 
    
def test_get2(hashtable):
    actual = hashtable.get("uljia")
    expected = "hass"
    assert actual == expected 


def test_get3(hashtable):
    actual = hashtable.get("salim")
    expected = "anwar"
    assert actual == expected 

def test_get4(hashtable):
    with pytest.raises(Exception):
        hashtable.get("tom")


def test_set1(hashtable):
    hashtable.set('martin', 'steve')
    actual=hashtable.contains('martin')
    expected = True
    assert actual == expected


def test_set2(hashtable):
    hashtable.set('martin', 'steve')
    actual=hashtable.get('martin')
    expected = 'steve'
    assert actual == expected

def test_hash(hashtable):
    actual=hashtable.hash('salim')
    expected = 886
    assert actual == expected


def test_hash2(hashtable):
    actual=hashtable.hash('julia')
    expected = 869
    assert actual == expected




@pytest.fixture
def hashtable():
    h=Hashtable()
    h.set('julia', 'Has')
    h.set('uljia', 'hass')
    h.set('salim', 'anwar')

    return h