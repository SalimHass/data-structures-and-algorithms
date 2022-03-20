import pytest
from data_structures_and_algorithms.linked_list import Node,LinkedList


def test_is_empty_linked_list():
    linked_list = LinkedList()
    expected = None
    actual = linked_list.head
    assert expected == actual

def test_insert_3_values(linked_list):
    expected = f"{{Flowers}}->{{For}}->{{Algernon}}->NULL"
    actual = linked_list.__str__()
    assert expected == actual

def test_include_for(linked_list):
    expected = True
    actual = linked_list.include("For")
    assert expected == actual

def test_append_3_values(linked_list2):
    expected = f"{{5}}->{{3}}->{{13}}->NULL"
    actual= linked_list2.__str__()
    assert expected == actual

def test_insert_before_values(linked_list3):
    expected = f"{{5}}->{{3}}->{{17}}->{{13}}->NULL"
    actual= linked_list3.__str__()
    assert expected == actual

def test_insert_after_values(linked_list4):
    expected = f"{{5}}->{{17}}->{{3}}->{{13}}->NULL"
    actual= linked_list4.__str__()
    assert expected == actual
    
def test_kth_element(linked_list4):
    expected = 17
    actual= linked_list4.kth_from_end(2).value
    assert expected == actual


@pytest.fixture
def linked_list():
    linked_list=LinkedList()
    linked_list.insert("Algernon")
    linked_list.insert("For")
    linked_list.insert("Flowers")
    return linked_list

@pytest.fixture   
def linked_list2():
    linked_list2=LinkedList()
    linked_list2.append(5)
    linked_list2.append(3)
    linked_list2.append(13)
    return linked_list2

@pytest.fixture
def linked_list3():
    linked_list3=LinkedList()
    linked_list3.append(5)
    linked_list3.append(3)
    linked_list3.append(13)
    linked_list3.insert_before(13,17)
    return linked_list3


@pytest.fixture
def linked_list4():
    linked_list4=LinkedList()
    linked_list4.append(5)
    linked_list4.append(3)
    linked_list4.append(13)
    linked_list4.insert_after(5,17)
    return linked_list4