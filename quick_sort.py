def quick_sort(source, left, right, direction='asc'):
 if left < right:
      pivot_idx = partition(source, left, right)
      quick_sort(source, left , pivot_idx - 1)
      quick_sort(source, pivot_idx + 1, right)

# [22, 11, 88, 66, 55, 77, 33, 44]

def partition(arr, left, right):
 i = left
 j = right - 1
 pivot_idx = right
 pivot_element = arr[pivot_idx]
 
 while i < j:
   while arr[i] < pivot_element and i < right:
     i += 1
   while arr[j] >= pivot_element and j > left:
     j -= 1
   if i < j:
    arr[i], arr[j] = arr[j], arr[i]

 if arr[i] > pivot_element:
  arr[i], arr[pivot_idx] = arr[pivot_idx], arr[i]

 return i


if __name__ == '__main__':
 source = eval(input('Enter source list: '))
 print(f'''
       Source list BEFORE sort: {source}''')
 quick_sort(source, 0, len(source)-1, direction='asc')
 print(f'''
       {' result '.upper().center(25, '*')}
       Source list AFTER sort: {source}
       ''')
 

# My version of partition using for loop
#  for i in range(left, pivot_idx + 1):
#   if arr[i] > pivot_element or i == pivot_idx:
#    for j in range(pivot_idx - 1, -1, -1):
#     if arr[j] < pivot_element or i == j:
#      if j <= i:
#       arr[i], pivot_element = pivot_element, arr[i]
#       return i
#      else:
#       arr[j] = arr[j], arr[i]
#       break