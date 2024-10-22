class SinglyLinkedList():
 def __init__(self) -> None:
  self.tail = self.head = None
  self.size = 0

 class Node():
  def __init__(self, value, prev=None) -> None:
   self.value = value
   self.prev = prev

 def addToHead(self, value):
  if self.size == 0:
   newNode = self.Node(value)
   self.tail = newNode
  else:
   newNode = self.Node(value)
   self.head.prev = newNode
  self.head = newNode
  self.size += 1

 def addToTail(self, value):
  if self.size == 0:
   newNode = self.Node(value)
   self.head = newNode
  else:
   newNode = self.Node(value, self.tail)
  self.tail = newNode
  self.size += 1

 def insert_node(self, value, before):
   curr = self.tail
   while curr.prev != None:
    if curr.value == before:
     newNode = self.Node(value, curr.prev)
     curr.prev = newNode
     self.size += 1
     return True
    curr = curr.prev
   return False
 
 def remove_node(self, value):
  if self.size == 0:
   return False
  curr = self.tail
  if curr.value == value:
   self.tail = curr.prev
   self.size -= 1
   return True
  while curr.prev != None:
   if curr.prev.value == value:
    if curr.prev == self.head:
     curr.prev = None
     self.head = curr
    else:
     curr.prev = curr.prev.prev
    self.size -= 1
    return True
   curr = curr.prev
  return False

   
   

 def __get_items(self):
  curr = self.tail
  list_str = []
  while curr.prev != None:
   list_str.append(curr.value)
   curr = curr.prev
  list_str.append(self.head.value)
  return ' <= '.join(reversed([str(node) for node in list_str]))

 def __repr__(self) -> str:
  if self.size != 0:
   return f'''
Size: {self.size}
Head at: {self.head.value}
Tail at: {self.tail.value}
Items: {self.__get_items()}
'''
  else:
   return 'The LinkList is EMPTY'
  
sll = SinglyLinkedList()
for i in range(50, 0, -10):
 sll.addToHead(i)
for i in range(60, 81, 10):
 sll.addToTail(i)
sll.insert_node(120, 40)
print(sll)
sll.remove_node(10)
print(sll)
sll.remove_node(120)
print(sll)