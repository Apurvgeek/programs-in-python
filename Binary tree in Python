#structure/class for a node
#by defult, left and right pointers are None 
class node:
  def __init__(self, val, left=None, right=None):
    self.left=left
    self.val=val
    self.right=right
 
 
#adding element in the binary tree
 
#create root node
root=node(4)
 
#add left child node to the root node
root.left=node(1)
 
#add right child node to the root node
root.right=node(5)
 
#similarly add other elements in the binary tree
root.left.left=node(7)
root.left.right=node(3)
root.right.right=node(6)
 
 
#reading value of binary tree nodes
 
#root node
print("Root node: ", root.val)
 
#left child of binary tree
print("Left child of root node: ", root.left.val)
 
#right child of binary tree
print("Right child of root node: ", root.right.val)
 
#similarly reding values of other binary tree nodes
print("Other node", root.left.left.val)
print("Other node", root.left.right.val)
print("Other node", root.right.right.val)
