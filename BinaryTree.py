class BinaryTree():
 def __init__(self, val):
  self.val = val
  self.l = None
  self.r = None 

 def insert_left(self, val):
  node = BinaryTree(val)
  if self.l:
   node.l = self.l
  self.l = node

 def insert_right(self, val):
  node = BinaryTree(val)
  if self.r:
   node.r = self.r
  self.r = node

 def setVal(self, node, new_val):
  node.val = new_val

 def is_leaf(self):
  return self.l == self.r == None
 
 def in_order(self):
  if self.l:
   self.l.in_order()
  print(self.val, end=',')
  if self.r:
   self.r.in_order()

 def size(self):
  if self.is_leaf():
   return 1
  if not self.l:
   return 1 + self.r.size()
  if not self.r:
   return 1 + self.l.size()
  return 1 + self.l.size() + self.r.size()
 
 def height(self):
  if self.is_leaf():
   return 0
  if not self.l:
   return 1 + self.r.height()
  if not self.r:
   return 1 + self.l.height()
  return 1 + max(self.l.height() , self.r.height())
 
 def get_left_subtree(self):
  return self.l
 
 def get_right_subtree(self):
  return self.r
 
 def isBTS(self):
  if self.is_leaf():
   return True
  if not self.l:
   return self.r.val > self.val and self.r.isBTS()
  if not self.r:
   return self.l.val < self.val and self.l.isBTS()
  return (self.r.val > self.val and self.r.isBTS()) and (self.l.val < self.val and self.l.isBTS())

 

tree = BinaryTree(9)

# Fill the tree
tree.insert_left(3)
tree.insert_right(10)
tree.get_right_subtree().insert_right(14)
tree.get_right_subtree().get_right_subtree().insert_left(13)
tree.get_left_subtree().insert_left(1)
tree.get_left_subtree().insert_right(6)
tree.get_left_subtree().get_right_subtree().insert_left(4)
tree.get_left_subtree().get_right_subtree().insert_right(7)
tree.get_left_subtree().get_right_subtree().get_right_subtree().insert_right(8)

# Check order, is is a Binary Search Tree, size, and height
print(f'Tree in-order:')
tree.in_order()
print(f'\nIs Binary Search Tree: {tree.isBTS()}')
print(f'size: {tree.size()}')
print(f'height: {tree.height()}')


