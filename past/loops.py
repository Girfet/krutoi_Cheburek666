i = 10
while i != 0:
  print(f'начало шага {11 - i}')
  command = input()
  if command == 'stop':
    break
  elif command == 'skip':
    continue 
  print(f'конец шага {11 - i}')
  i -= 1
else:
  print('finish')

for i in range(1,11):
  print(f'начало шага {i}')
  command = input()
  if command == 'stop':
    break
  elif command == 'skip':
    continue 
  print(f'конец шага {i}')
else: #срабатывает , если цикл закончился без прерывания
  print('finish')