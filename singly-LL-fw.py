class SinglyLinkedList():
 class Node():
  def __init__(self, value, next=None):
   self.value = value
   self.next = next

 def __init__(self):
  self.head = self.tail = None
  self.size = 0

 def addToHead(self, value, next=None):
  if self.size == 0:
   newNode = self.Node(value)
   self.tail = newNode
  else:
   newNode = self.Node(value, self.head)
  self.head = newNode
  self.size += 1

 def addToTail(self, value):
  if self.size != 0:
   newNode = self.Node(value)
   self.tail.next = newNode
  else:
   newNode = self.Node(value)
   self.head = newNode
  self.tail = newNode
  self.size += 1
 
 def insert_node(self, value, before):
  curr = self.head
  while curr.next != None:
   if curr.next.value == before:
    newNode = self.Node(value, curr.next)
    curr.next = newNode
    self.size += 1
    return True
   curr = curr.next
  return False

 def remove_node(self, value):
  curr = self.head
  if self.size == 0:
    return False
  while curr.next != None:
    if curr.next.value == value:
      curr.next = curr.next.next
      self.size -= 1
      return True
    curr = curr.next
  return False

 def __get_items(self):
  if self.size != 0:
   list_str = ''
   curr= self.head
   while curr.next != None:
    list_str += str(curr.value) + ' => '
    curr = curr.next
   list_str += str(curr.value)
   return list_str
  else:
   return 'The List is EMPTY'
  
 def print_items(self):
  print(self.__get_items())

 def __repr__(self) -> str:
  if self.size != 0:
   return f'''
   Size: {self.size}
   Head at: {self.head.value}
   Tail at: {self.tail.value}
   Items: {self.__get_items()}
         '''
  else:
   return 'The List is EMPTY'


sll = SinglyLinkedList()
for i in range(50, 0, -10):
 sll.addToHead(i)
for i in range(60, 90, 10):
 sll.addToTail(i)
sll.insert_node(130,40)
print(sll)
sll.remove_node(130)
print(sll)