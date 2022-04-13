import pytest
from data_structures_and_algorithms.trees import TNode,BinaryTree,BinarySearchTree

def test_tree_post_order(tree):
  actual = tree.post_order()
  expected = [6,7,2,5,4,3,1]
  assert actual == expected


def test_tree_root(tree):
  actual = tree.root.value
  expected = 1
  assert actual == expected


def test_b_tree(b_tree):
        
    actual = b_tree.post_order()
    expected = [5, 3, 7, 13, 10]
    assert actual == expected

def test_b_tree_true(b_tree):
    actual = b_tree.contains(7)
    expected = True
    assert actual == expected 


def test_b_tree_true(b_tree):
    actual = b_tree.contains(27)
    expected = False
    assert actual == expected 






@pytest.fixture
def tree():
 
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node5=TNode(5)
    node6=TNode(6)
    node7=TNode(7)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    node3.left=node5
    node2.left=node6
    node2.right=node7
    tree=BinaryTree()
    tree.root=node1

    return tree


@pytest.fixture
def b_tree():
    b_tree=BinarySearchTree()
    b_tree.add(10)
    b_tree.add(7)
    b_tree.add(3)
    b_tree.add(5)
    b_tree.add(13)

    return b_tree