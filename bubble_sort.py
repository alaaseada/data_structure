def bubble_sort(source):
 for limit in range(len(source) - 1, 0, -1):
  swaps = 0
  for i in range(limit):
   if source[i] > source[i + 1]:
    source[i], source[i+1] = source[i+1], source[i]
    swaps += 1
  if swaps == 0:
   break
    



if __name__ == '__main__':
 source = eval(input('Enter source list: '))
 print(f'''
       Source list BEFORE sort: {source}''')
 bubble_sort(source)
 print(f'''
       {' result '.upper().center(25, '*')}
       Source list AFTER sort: {source}
       ''')