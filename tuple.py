#кортеж - tuple           НЕИЗМЕНЯЕМЫЙ СПИСОК
numbers = (28, 44, 67)
print(numbers)
print(len(numbers))
print(numbers[0])
print(numbers[::-1])

# numbers[1] = 55      элементы кортежа
# print(numbers)       изменять нельзя

#константа - неизменяемая переменная
BLACK = (0, 0, 0)
WHITE = 255, 255, 255
print(WHITE)
R, G, B = (223, 124, 95)
a, b = ['cat', 'dog']
BROWN = R, G ,B 

test = (6,)
print(test)

