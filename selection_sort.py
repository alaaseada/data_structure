def selection_sort(source, direction='asc'):
 operator = '>' if direction == 'desc' else '<'
 for i in range(0, len(source)):
  indicator = i
  for j in range(indicator + 1, len(source)):
   if eval(f'source[j] {operator} source[indicator]'):
    indicator = j
  source[i], source[indicator] = source[indicator], source[i]
   



if __name__ == '__main__':
 source = eval(input('Enter source list: '))
 print(f'''
       Source list BEFORE sort: {source}''')
 selection_sort(source, direction='asc')
 print(f'''
       {' result '.upper().center(25, '*')}
       Source list AFTER sort: {source}
       ''')