def selectionSort(alist):
 for i in range(len(alist) - 1, 0, -1):
  print(i)
 for fill_slot in range(len(alist) - 1, 0, -1):
  pos_of_max = 0
  for location in range(1, fill_slot + 1):
   if alist[location] > alist[pos_of_max]:
    pos_of_max = location
  temp = alist[fill_slot]
  alist[fill_slot] = alist[pos_of_max]
  alist[pos_of_max] = temp

 # for fill_slot in range(len(alist) - 1, 0, -1):
 #  pos_of_max = 0
 #  for location in range(1, fill_slot + 1):
 #   if alist[location] > alist[pos_of_max]:
 #    pos_of_max = location
 #  if alist[pos_of_max] > alist[fill_slot]:
 #   alist[fill_slot], alist[pos_of_max] = alist[pos_of_max], alist[fill_slot]


 
test_list = [26, 54, 93, 17, 77, 31, 44, 55, 20]
selectionSort(test_list)
print(test_list)