# Binary Tree and BST Implementation 

1. create a class Node that stores a value and a left child node and right child node
2. create binary tree class, it should contain the methods for the depth first traversal: pre order, in order and post order, post order should return an array
3. create binary search tree class, it should be a subclass lf the binary tree class, and should contain these methods, 

        i- add:takes a value as an argument , and adds the value as new node in three where is should be.

        ii- contains: takes a value as an argument, return a boolean whether the value is in the list or not. 


## Whiteboard Process
![whiteboard](../data_structures_and_algorithms/assessts/Tree.jpg)



## Approach & Efficiency
we used the recursion as inner function to traverse each tree and track its values. And inside that recursive function, we got the value we want and appended it to a list.

Big-O for the methods:

- pre_order 
    - BigO for time = n 
    - BigO for space = n  

- in_order
    - BigO for time = n 
    - BigO for space = n   

- post_order
    - BigO for time = n 
    - BigO for space = n 
    
- add
    - BigO for time = n  
    - BigO for space = 1 

- contains
    - BigO for time = n 
    - BigO for space= 1



## API

### BinaryTree class

pre_order

    Input: None
    doing: traverse a tree (pre-order --> root-left-right)
    output: print values of the nodes of the tree

in_order

    Input: None
    doing: traverse a tree (in-order --> left-root-right)
    output: print values of the nodes of the tree


post_order

    Input: None
    doing: traverse a tree (post-order --> left-right-root)
    output: print values of the nodes of the tree

### BinaryTreeSearch class

add

    input: value
    doing: add the value correctly to the tree
    output: None

contains
   
    input: value
    doing: check if the value is in the tree at least once
    output: boolean 