# словарь - dictionary (dict)
a = {}   # пустой словарь
b = set()  # пустое множество
# ключ: значение
# key: value
fridge = {'огурец': 2, 'помидор': 3, 'трюфель': 7}
print(len(fridge))

# достать значение по ключу
print(fridge['трюфель'])

# изменить значение по ключу
fridge['огурец'] = 82
print(fridge)

# добавить ключ - значение
fridge['ъ'] = 98
print(fridge)

# удалить ключ - значение
fridge.pop('помидор')
print(fridge)
del fridge['трюфель']
print(fridge)

#Оператор in (По ключам!!!)
print('огурец' in fridge)