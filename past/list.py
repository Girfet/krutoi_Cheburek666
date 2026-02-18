# list - список
students = ['Абрамов', 'Тимофеев', 'Сардарян', 'Тимофеев']
# Индексы
print(students[0])
print(students[2])
print(students[::-1])
# длина списка
print(len(students))
# оператор in
if 'Тимофеев' in students:
    print('yes')

# изменить элемент
students[0] = 'Казимирчик' 
print(students)

# Добавить элемент
students.append('Семыкин')
print(students)

# удалить элемент
# del students[3]
# students.pop()   удаляет последнюю
# del_student = students.pop(2) 
students.remove('Тимофеев')
print(students)

a = [1, 2, 3] + [4, 5 ,6]
print(a)
a += [7, 8, 9]
print(a)
print(a * 2)
