
from data_structures_and_algorithms.hashtable import Hashtable
from data_structures_and_algorithms.trees import TNode,BinaryTree



def tree_intersection (tree1,tree2):
    arr=[]
    htable=Hashtable()
    if not tree1.root or not tree2.root:
        raise Exception("one of the trees or both are empty")
    
    def _walk(node1, node2):
        
        if node1.value==node2.value:
            htable.set(str(node1.value), None)
        
        if node1.left and node2.left:
            _walk(node1.left,node2.left)
        if node1.right and node2.right:
            _walk(node1.right,node2.right)
    
    _walk(tree1.root,tree2.root)
    return htable.keys()
        


if __name__=="__main__":
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

    tree2= BinaryTree()
    tree2.root= node1

    print(tree_intersection(tree1,tree2))


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
    print(tree_intersection(tree1,tree3))    