# name = input("Как тебя зовут?:\n")
# print("Приятно познакомится,", name)
# age = int(input("Сколько тебе лет?:\n"))
# new_age = age + 5
# print("Через 5 лет тебе будет", new_age)

# # То же самое можно сделать в 1 строку
# print("Приятно познакомится,", 
#       input("Как тебя зовут?:\n"), 
#       "\nЧерез 5 лет тебе будет", 
#       int(input("Сколько тебе лет?:\n")) + 5)


# a = int(input())
# # Идея 1: все четные кончаются на 0, 2, 4, 6, 8
# # if a % 10 == 0:
# #   print("четное")
# # if a % 10 == 2:
# #   print("четное")
# # ...


# # Идея 2: надо сравнить результат деления нацело и обычного деления
# if a // 2 == a / 2:
#   print('чётное')
# else:
#   print('нечётное')

# # Идея 3: число делится ПОЛНОСТЬЮ, а значит не будет остатка
# if a % 2 == 0:
#   print('чётное')
# else:
#   print('нечётное')

# b = 1 
# s = 0
# while b <= 100:
#   s += b
#   b += 1
# print(s)
# for char in "ABCDEFGH":
#  for i in range(1,9):
#    print(char + str(i))
# for i in range(100,0,-1):
#    print(i)

# n = int(input())
# count = 0
# sum_ = 0
# while n != 0:
#   if n % 10 == 1:
#    sum_ += n
#    count += 1
#   n = int(input())
# if count == 0:
#   print('NO')
# else:
#   print(sum_/count)

# for i in range(5):  #3 1 5 3 7 
#   if i % 2 == 0:   
#     i += 3
#   print(i)
# flag = False 
# for i in range(5):
#   n = int(input())
#   if n == 0:
#     flag = True
#     break
# if flag:
#   print('yes')
# else:
#   print('no')

# for i in range(5):
#   n = int(input())
#   if n == 0:
#     print('yes')
#     break
# else:
#   print('no')

# text = input()
# char = input()
# while len(char) != 1 or not char.isalpha():
#     char = input('Введите 1 букву: ')
# print(text.count(char))
# new_char = input('введите новую букву: ')
# while len(new_char) != 1 or not new_char.isalpha():
#     new_char = input('Введите 1 букву: ')
# text = text.replace(char, new_char)
# print(text)

# Выбор рандомного события
# import random 
# events = ['Аннексия', 'Сделать марионеткой', 'Изменение правительства']
# # index = random.randint(0, len(events) - 1)
# # print(events[index])
# print(random.choice(events))
# # инвентарь
# inventory = []
# while True:
#     command = input('1.Положить в инвентарь 2.Убрать из инвентаря 3.Выход')
#     if command == '1':
#         item = input('Что положить?')
#         inventory.append(item)
#         print(inventory)

#
# word = input()
# # bukvi = {word[0]} 
# bukvi = set()
# for i in word:
#     bukvi.add(i)
# print(len(bukvi))
print(len(set(input())))
