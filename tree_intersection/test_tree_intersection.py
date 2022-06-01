import pytest
from data_structures_and_algorithms.trees import TNode,BinaryTree

from tree_intersection import tree_intersection

def test_tree_intersection(tree1,tree2):
  actual = tree_intersection(tree1,tree2)
  expected = ['50', '26', '1', '2', '3', '5', '7']
  assert actual == expected

def test_tree_intersection2(tree1,tree3):
  actual = tree_intersection(tree1,tree3)
  expected = ['50', '1', '2', '3', '7']
  assert actual == expected

def test_tree_intersection_empty(tree1,tree4):
  with pytest.raises(Exception):
        tree_intersection(tree1,tree4)


def test_tree_intersection_none(tree1,tree5):
  actual = tree_intersection(tree1,tree5)
  expected = []
  assert actual == expected





@pytest.fixture
def tree1():
 
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(26)
    node5=TNode(5)
    node6=TNode(50)
    node7=TNode(7)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    node3.left=node5
    node2.left=node6
    node2.right=node7
    tree1 = BinaryTree()
    tree1.root=node1

    

    return tree1


@pytest.fixture
def tree2():
 
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(26)
    node5=TNode(5)
    node6=TNode(50)
    node7=TNode(7)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    node3.left=node5
    node2.left=node6
    node2.right=node7
    tree2 = BinaryTree()
    tree2.root=node1

    return tree2

@pytest.fixture
def tree3():
 
    node10 = TNode(1)
    node20 = TNode(2)
    node30 = TNode(3)
    node40 = TNode(26)
    node50=TNode(5)
    node60=TNode(50)
    node70=TNode(7)
    node10.left = node20
    node10.right = node30
    node30.left = node40
    node30.right=node50
    node20.left=node60
    node20.right=node70
    tree3=BinaryTree()
    tree3.root=node10

    return tree3


@pytest.fixture
def tree4():
  tree4=BinaryTree()
  tree4.root=None

  return tree4

@pytest.fixture
def tree5():
 
    node1 = TNode(10)
    node2 = TNode(20)
    node3 = TNode(30)
    node4 = TNode(260)
    node5=TNode(50)
    node6=TNode(500)
    node7=TNode(70)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    node3.left=node5
    node2.left=node6
    node2.right=node7
    tree5 = BinaryTree()
    tree5.root=node1

    return tree5