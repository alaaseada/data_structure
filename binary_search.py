def binary_search(keyword, source):
 low = 0
 high = len(source) - 1
 n_steps = 0

 while low <= high:
  n_steps += 1
  mid = low + ((high - low) // 2)
  if keyword > source[mid]:
   low = mid + 1
  elif keyword < source[mid]:
   high = mid - 1
  else:
   return [mid, n_steps]
 return [None, n_steps]


def printValues(grades, keyword, idx, n_steps):
 print(f'''
   Source sorted list: {grades}
   keyword: {keyword}''')
 if idx:
   print(f'''
   {' Result '.upper().center(25, '*')}
   Index: {idx}
   Length of list: {len(grades)}
   Found after: {n_steps} steps''')
 else:
   print(f'''
  {' Result '.upper().center(25, '*')}
  {keyword} is Not Found
  Number of steps: {n_steps} steps''')

def handle_input_list(source_list, type_of_list):
 if type_of_list == 'str':
  return sorted([item.title() for item in source_list], key=str.casefold)
 else:
  return sorted(source_list)

def handle_keyword(keyword):
 if keyword == 'x':
   return 'exit'
 if type_of_list == 'int':
   return int(keyword)
 elif type_of_list == 'float':
   return float(keyword)
 else:
  return keyword.title()
 
if __name__ == '__main__':
 exit = False
 source_list = eval(input('Source list: '))
 type_of_list = input('Type of list int, float [default str]: ')
 if type_of_list not in ['int', 'float']: 
  type_of_list = 'str'
 source_list = handle_input_list(source_list, type_of_list)
 while not exit:
  keyword = handle_keyword(input('\nItem to search for (or x to exit): '))
  if keyword == 'exit':
   break
  idx, n_steps = binary_search(keyword, source_list)
  printValues(source_list, keyword, idx, n_steps)
  