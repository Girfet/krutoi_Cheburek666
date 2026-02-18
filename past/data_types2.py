# булевый тип данных (логический тип данных)- boolean -bool 
alive = False
print(type(alive))

if alive:
  print('ничего')
else:
  print('перезагрузить уровень')



a = 5
# |    bool    |
# ( int )  (int)
if a % 2 == 0: # знаки == != <= >= < > дают тип данных bool
  print("even")
else:
  print("odd")


print(5 > 0)
print("cat" == "Cat")
print(4 != 7)