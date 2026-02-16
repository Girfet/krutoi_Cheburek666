text = 'Я изучаю Пайтон!'
# Конкатенация 
# print(text + 'яблоко')
# print('ааа женщина тревога'*5)
# # цикл по символам
# for h in text:
#     print(h)
# индекс - номер элемента
# print(text[0])
print(text[-7])
# срез (slice) - Кусок строки от одного индекса до другого
print(text[0:8])
print(text[9:16])
# конец диапазона не включительно
print(text[:8])
print(text[9:])
print(text[:100])
#можно добавить шаг
print(text[0:16:2])
print(text[-1:-17:-1])
print(text[:])
print(text[::-1])
# text[0] = 'Ы' элементы строки менять нельзя
print(text)
print('\n')

#оператор in 
print('Я' in text)
if 'Я' in text:
    print('yes')
#!!!!!!!!!!!!!!!!!!!!!! len кол-во элементов !!!!!!!!!!!!!!!!!!!! 
print(len(text))

# методы str
# функция, которая вызывается при помощи точки после объекта
#изменение регистра
print(text.lower())

print(text.upper())

print(text.title())

#подсчёт количества определённых символов
print(text.count('а'))
print(text.count('Пайтон'))

#заменить одну подстроку на другую 
print(text.replace('Пайтон', 'C++'))

