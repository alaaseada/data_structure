def heapify(arr, n , i):
 largest = i
 left = 2 * i + 1
 right = 2 * i + 2

 if left < n and arr[left] > arr[i]:
  largest = left

 if right < n and arr[right] > arr[largest]:
  largest = right 

 if largest != i:
  arr[largest], arr[i] = arr[i], arr[largest]
  heapify(arr, n , largest)

# ==============
def build_max_heap(arr, n):
 for i in range(n//2, -1, -1):
  heapify(arr, n, i)

# =============
def heap_sort(arr):
  n = len(arr)
  for i in range(n-1 , 0, -1):
   build_max_heap(arr, i)
   if arr[0] > arr[i]:
    arr[i], arr[0] = arr[0], arr[i]
    
# ============
if __name__ == '__main__':
 arr = [13, 15, 32, 16, 44, 100, 71, 2, 1, 20, 30]
 print('Original array= ', arr)
 heap_sort(arr)
 print('Heap Sorted = ', arr)