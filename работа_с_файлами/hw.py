# print('Предложения SkysmartBank')
# print(open('suggestions.txt', 'r', encoding = 'utf-8').read())

f = open('suggestions.txt', 'w', encoding = 'utf-8')

name = input('Введите пользователя:   ')
f.write('Пользователь: ' + name)
f.close
