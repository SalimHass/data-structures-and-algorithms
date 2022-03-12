import pytest
from data_structures_and_algorithms.linked_list import Node,LinkedList


def test_is_empty_linked_list():
    linked_list = LinkedList()
    expected = None
    actual = linked_list.head
    assert expected == actual

def test_insert_3_values(linked_list):
    expected = f"Flowers->For->Algernon->NULL"
    actual = linked_list.__str__()
    assert expected == actual




@pytest.fixture
def linked_list():
    linked_list=LinkedList()
    linked_list.insert(Node("Algernon"))
    linked_list.insert(Node("For"))
    linked_list.insert(Node("Flowers"))
    return linked_list