# set - множество

fruit = {'apelsin', 'mandarin', 'Durian', 'Jabloko'}
orange = {'apelsin', 'mandarin', 'markov', 'cot', 'apelsin', 'apelsin'}
print(len(orange))
print(orange)

#У множества нет порядка

#добавить эелемент
fruit.add('melon')
print(fruit)

#убрать элемент
# fruit.remove('mandarin')
# print(fruit)
# a = fruit.pop()
# print(a)
# print(fruit)

#операции со множествами
# пересечение
print(fruit.intersection(orange))
print(fruit & orange)

#объединение
print(fruit.union(orange))
print(fruit | orange)

#разница
print(fruit.difference(orange))
print(fruit - orange)