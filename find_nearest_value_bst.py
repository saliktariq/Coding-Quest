"""
# Find Closest Value In BST

Write a function that takes in a Binary Search Tree (BST) and a target integer value 
and returns the closest value to that target value contained in the BST.

You can assume that there will only be one closest value.

Each BST node has an integer value, a left child node, and a right child node. 
A node is said to be a valid BST node if and only if it satisfies the BST property: 
its value is strictly greater than the values of every node to its left; 
its value is less than or equal to the values of every node to its right; 
and its children nodes are either valid BST nodes themselves or None / null.

## Sample Input

```
   tree =    10
           /     \
          5      15
        /   \   /   \
       2     5 13   22
     /           \
    1            14
    
   target = 12
```

## Sample Output

```
13
```
"""
from bst import BST

tree = BST()
for v in [10, 5, 15, 2, 5, 13, 22, 1, 14]:
    tree.insert(v)



def find_nearest_value_bst(t: BST, v: int) -> int | None:
    delta = None
    node = None

    if t is None:
        return

    current_node = t.root

    while current_node is not None:
        d = abs(current_node.value - v)
        if delta is None or d < delta:
            delta = d
            node = current_node
        if v < current_node.value:
            current_node = current_node.left
        else:
            current_node = current_node.right
    return node.value

print(find_nearest_value_bst(tree, 12))




            




                

