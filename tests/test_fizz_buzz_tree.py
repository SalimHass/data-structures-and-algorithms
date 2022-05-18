import pytest
from data_structures_and_algorithms.trees import KNode,KTree,fizz_buzz_tree

def test_fizz_buzz_tree(ktree):
    expected = [13, 'Buzz', 'FizzBuzz', 'Fizz', 'FizzBuzz', 17, 'Fizz']
    actual = fizz_buzz_tree(ktree).breadth()
    assert expected == actual

def test_fizz_buzz_tree_empty():
    with pytest.raises(Exception):
        fizz_buzz_tree()



@pytest.fixture
def ktree():
    node1=KNode(13)
    node2=KNode(15)
    node3=KNode(17)
    node4=KNode(21)
    node5=KNode(25)
    node6=KNode(24)
    node7=KNode(30)
    node1.children=[node5,node7]
    node5.children=[node4]
    node7.children=[node2, node3]
    node3.children=[node6]
    ktree=KTree()
    ktree.root=node1
    ktree.breadth()
    fizz_buzz_tree(ktree).breadth()
    return ktree
