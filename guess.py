import random 
#бинарный поиск

number = random.randint(1, 1000)

attempts = 10

while attempts != 0:
  
  user_number = input('Введите число: ')
  
  if not user_number.isdigit(): #Проверка на то, что в ответе присутсвуют только цифры
    print('Вводите только число')
    # перейти на следующий шаг цикла 
    continue
    
  user_number = int(user_number)
  
  if number == user_number:
    print('Ты угадал')
    # Прервать цикл
    break
  else:
    attempts -= 1 
    
    if number > user_number:
      print('Больше')
    else:
      print('Меньше')
      
if attempts == 0:
  print(f'ты проиграл, загаданное число было {number}.')