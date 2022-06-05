from sorting.quick.quick import quick_sort
import pytest

def test_quick_sort1():
    actual = [4, 8, 15, 16, 23, 42]
    expexted= quick_sort([8,4,23,42,16,15],0,5)
    assert expexted==actual

def test_quick_sort2():
    actual = [-2, 5, 8, 12, 18, 20]
    expexted= quick_sort([20,18,12,8,5,-2],0,5)
    assert expexted==actual

def test_quick_sort3():
    actual = [5, 5, 5, 7, 7, 12]
    expexted= quick_sort([5,12,7,5,5,7],0,5)
    assert expexted==actual

def test_quick_sort4():
    actual =  [2, 3, 5, 7, 11, 13]
    expexted= quick_sort([2,3,5,7,13,11],0,5)
    assert expexted==actual

def test_merge_sort_empty():
    with pytest.raises(Exception):
        quick_sort([],0,5)


def test_quick_sort_none():
    with pytest.raises(Exception):
        quick_sort(None,0,5)

def test_quick_sort_right_greater_length():
    with pytest.raises(Exception):
        quick_sort([2,3,5,7,13,11],0,7)

