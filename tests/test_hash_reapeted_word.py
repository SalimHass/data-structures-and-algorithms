import pytest
from data_structures_and_algorithms.hashtable import  repeated_word



def test_empty():
    with pytest.raises(Exception):
        repeated_word("")

def test_unique():
    with pytest.raises(Exception):
        repeated_word("this is the end")

def test_text1():
    actual=repeated_word('Once upon a time, there was a brave princess who...')
    expected = "a"
    assert actual == expected

def test_text2():
    actual=repeated_word('It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...')
    expected = 'it'
    assert actual == expected

def test_text3():
    actual=repeated_word('It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...')
    expected = 'summer'
    assert actual == expected