import pytest
from data_structures_and_algorithms.hashtable import Hashtable
from hashmap_left_join import left_join


def test_hashmap_left_join1(map1, map2):
    actual=left_join(map1,map2)
    expected = [['fond', 'enamored', 'averse'], ['outfit', 'garb', None], ['diligent', 'employed', 'idle'], ['wrath', 'anger', 'delight'], ['guide', 'usher', 'follow']]
    assert actual == expected
def test_hashmap_left_join(map1, map2):
    actual=left_join(map1,map2)
    expected = [['fond', 'enamored', 'averse'], ['outfit', 'garb', None], ['diligent', 'employed', 'idle'], ['wrath', 'anger', 'delight'], ['guide', 'usher', 'follow']]
    assert actual == expected
def test_hashmap_left_join_none(map1, map2):
    actual=left_join(map1,map2)[1][2]
    expected = None
    assert actual == expected

def test_hashmap_left_join2(map1, map2):
    actual=left_join(map1,map2)[0][2]
    expected = 'averse'
    assert actual == expected

def test_hashmap_left_join3(map1, map2):
    actual=left_join(map1,map2)[2][1]
    expected = 'employed'
    assert actual == expected    

def test_hashmap_left_join_length(map1, map2):
    actual=len(left_join(map1,map2))
    expected = 5
    assert actual == expected    

def test_hashmap_left_join_length_elem(map1, map2):
    actual=len(left_join(map1,map2)[1])
    expected = 3
    assert actual == expected 

@pytest.fixture
def map1():
    h1=Hashtable()
    h1.set('diligent','employed')
    h1.set('fond','enamored')
    h1.set('guide','usher')
    h1.set('outfit','garb')
    h1.set('wrath','anger')

    return h1

@pytest.fixture
def map2():   
    h2=Hashtable()
    h2.set('diligent','idle')
    h2.set('fond','averse')
    h2.set('guide','follow')
    h2.set('flow','jam')
    h2.set('wrath','delight')

    return h2