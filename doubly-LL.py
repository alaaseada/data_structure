class DoublyLinkedList():
 def __init__(self) -> None:
  self.head = self.tail = None
  self.size = 0

 class Node():
  def __init__(self, value, prev=None, next=None) -> None:
   self.value = value
   self.prev = prev
   self.next = next

 # Add a node to the head of the linkedList
 def addToHead(self, value):
  if self.size == 0:
   newNode = self.Node(value)
   self.tail = newNode
  else:
   newNode = self.Node(value, next=self.head)
   self.head.prev = newNode
  self.head = newNode
  self.size += 1

 # Add a node to the tail of the linkedList
 def addToTail(self, value):
  if self.size == 0:
   newNode = self.Node(value)
   self.head = newNode
  else:
   newNode = self.Node(value, prev=self.tail)
   self.tail.next = newNode
  self.tail = newNode
  self.size += 1

 # Insert a node before an element in the linkedList
 def insert_node(self, value, before):
  idx = 0
  curr = self.head
  while idx < self.size:
   if curr.value == before:
    newNode = self.Node(value)
    if curr.prev == None:
     newNode.next = self.head
     self.head.prev = newNode
     self.head = newNode
    else:
     newNode.next = curr
     newNode.prev = curr.prev
     curr.prev = newNode
     newNode.prev.next = newNode
    self.size += 1
    return True
   curr = curr.next
   idx += 1
  return False
 
 # Remove a node from the linkedList
 def remove_node(self, value):
  if self.size == 0:
   return False
  idx = 0
  curr = self.head
  while idx < self.size:
   if curr.value == value:
    if self.size == 1:
     self.head = self.tail = None
    elif curr == self.head:
     self.head = curr.next
     curr.next.prev = None
    elif curr == self.tail:
     self.tail = curr.prev
     curr.prev.next = None
    else:
     curr.prev.next = curr.next
     curr.next.prev = curr.prev
    self.size -= 1
    return True
   curr = curr.next
   idx += 1
  return False
    
 def find(self, value, all=True):
  slots = []
  if self.size == 0:
   return slots
  idx = 0
  num_of_occurence = 0
  curr = self.head
  while idx < self.size:
   if curr.value == value:
    num_of_occurence += 1
    slots.append(idx)
    if not all:
     break
   idx += 1
   curr = curr.next
  return slots

 # Get the linkedList's elements
 def __get_items(self):
  idx = 0
  curr = self.head
  list_str = []
  while idx < self.size:
   list_str.append(curr.value)
   curr = curr.next
   idx += 1
  return ' <==> '.join([str(node) for node in list_str])


 # Implement the __repr__ magic method to print the linkedList
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
  

# Test cases 
dll = DoublyLinkedList()

# Add to head
print('Add 10, 20, 30, 40, and 50 to Head')
for i in range(50, 0, -10):
 dll.addToHead(i)
print(dll)

# Add to tail
print('Add 60, 70, and 80 to Tail')
for i in range(60, 81, 10):
 dll.addToTail(i)
print(dll)

# Insert values
print('Insert values 100, 300, 500, 700, 900 before tens of these values')
not_added = []
for i in range(10, 91, 20):
 result = dll.insert_node(i * 10, i)
 if not result:
  not_added.append(i * 10)
print(dll)
if len(not_added):
 print(f'Values {not_added} not added because {[i//10 for i in not_added]} is/are not in the List')
 
# Remove a value
dll.remove_node(100)
print(dll)

dll.insert_node(20, 700)
print(dll)

# Find an element in the LinkedList
val = 35
slots = dll.find(val, all=False)
print(f'Slots where node value {val} is found= {slots}')






  
  # curr = self.head
  # list_str = []
  # while curr.next != None:
  #  next = str(curr.next.value) if curr.next else 'None'
  #  prev = str(curr.prev.value) if curr.prev else 'None'
  #  tail_next = str(self.tail.next.value) if self.tail.next else 'None'
  #  list_str.append(prev+ ':' + str(curr.value) + ':' + next )
  #  curr = curr.next
  # list_str.append(str(self.tail.prev.value) + ':' + str(self.tail.value) + ':' + tail_next)
  # return ' <==> '.join(list_str)