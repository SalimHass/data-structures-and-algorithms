from curses import nonl
from logging import root


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
        def _walk(node):
            print(node.value)

            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(self.root)
    
    def in_order(self):
        """
    Input: None
    doing: traverse a tree in_order
    output: print values of the nodes of the tree
    """
        def _walk(node):
            
            if node.left:
                _walk(node.left)
            print(node.value)
            if node.right:
                _walk(node.right)

        _walk(self.root)

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

        
    
        
    
        


if __name__== "__main__":
    
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

    tree = BinaryTree()
    tree.root = node1
    #tree.in_order()
    #print(tree.post_order())
    bin= BinarySearchTree()
    bin.add(10)
    bin.add(7)
    bin.add(3)
    bin.add(5)
    bin.add(13)
    print(bin.post_order())

    print(bin.contains(6))
    

