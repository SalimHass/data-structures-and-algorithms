from locale import currency
from pickle import FALSE
from platform import node
import queue
from data_structures_and_algorithms.stack_and_queue import Queue
class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        """
    Input: None
    doing: traverse a tree pre_order
    output: print values of the nodes of the tree
    """
        arr=[]
        def _walk(node):
            arr.append(node.value)

            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(self.root)
        return arr
    
    def in_order(self):
        """
    Input: None
    doing: traverse a tree in_order
    output: print values of the nodes of the tree
    """
        arr=[]
        def _walk(node):
            
            if node.left:
                _walk(node.left)
            arr.append(node.value)
            if node.right:
                _walk(node.right)

        _walk(self.root)
        return arr

    def post_order(self):
        """
        Input: None
        doing: traverse a tree post order
        output: list of the values
        """
        arr=[]
        def _walk(node):
            if node.left:
                _walk(node.left)
            
            if node.right:
                _walk(node.right)
            
            arr.append(node.value)
            
                
        _walk(self.root)
        return arr
    


def find_max(root):
    max= root.value
    def _walk(node):
        nonlocal max
        if node.value > max:
            max=node.value
        if node.left:
            _walk(node.left)
        if node.right:
            _walk(node.right)

    _walk(root)
    return max

def breadth_first(root):
    q=Queue()
    arr=[]
    q.enqueue(root)
    
    
    while q.front:
        arr.append(q.front.value.value)
        
        if q.front.value.left is not None:
            q.enqueue(q.front.value.left)
        if q.front.value.right is not None:
            q.enqueue(q.front.value.right)

        q.dequeue()
    return arr
    

       
        
 

        
class BinarySearchTree(BinaryTree):

    def __init__(self):
        super().__init__()

    def add(self, value):
        if self.root is None:
            self.root = TNode(value)
            return
        node = self.root
        while node:
            if node.value >= value:
                if node.left is None:
                    node.left = TNode(value)
                    return
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = TNode(value)
                    return
                else:
                    node = node.right

    def contains(self, value):
        return value in self.post_order()

        
    
        
class KNode:
    def __init__(self, value):
        """this takes a value as arg , and will create a node with possible children"""
        self.value = value
        self.children=[]

class KTree:
    def __init__(self):
        self.root=None
    
    def breadth(self):
        if self.root is None:
            return "Empty Tree"
        current = self.root
        elements = []
        q = Queue()
        q.enqueue(current)
        while q.front is not None :
            current=q.dequeue()
            elements.append(current.value)
            for child in current.children:
                q.enqueue(child)
        print(elements)    
        return elements

    def adding_child(self, value, parent):
        new_node=KNode(value)
        parent.children.append(new_node)
        return new_node

    

def fizz_buzz_tree(k_tree):
    new_tree=KTree()
    if k_tree.root is None:
        raise Exception('tree is empty')

    def _walk(current , parent = None):
        if current.value % 3 == 0 and current.value % 5 == 0:
            new_value = 'FizzBuzz'

        elif current.value % 3 == 0:
            new_value = 'Fizz'
        elif current.value % 5 == 0:
            new_value = 'Buzz'
        else:
            new_value = current.value

        node= KNode(new_value)
        if parent is not None :
            parent.children.append(node)
        if current.children:
            for child in current.children:
                _walk(child,node)

        if parent is None:
            return node
        
    new_tree.root=_walk(k_tree.root)

    return new_tree
            









        


if __name__== "__main__":

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

""" node1 = TNode(1)
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
    tree = BinaryTree()
    tree.root = node1
    #tree.pre_order()

    print(find_max(node1))

    #tree.in_order()
    #print(tree.post_order())
    bin= BinarySearchTree()
    bin.add(10)
    bin.add(7)
    bin.add(3)
    bin.add(5)
    bin.add(13)
    #print(bin.post_order())
    #print(bin.contains(6))

    print(tree.breadth_first())"""
    
    





