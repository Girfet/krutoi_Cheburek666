# авршпербер
[[главное меню]]
---
![дракониха из шрека](https://avatars.mds.yandex.net/i?id=6a4e7d6d213932f9a4b0149baf4c062fcd5d039f-12413751-images-thumbs&n=13)

```python
import time
import random

print('Добро пожаловать в игру "Угадай загадку"!')
RIDDLES = ['Каких камней нет в море?', 'Что нельзя съесть на завтрак?',
'У вас есть только одна спичка. В тёмной комнате стоят керосиновая лампа, печь и свеча. Что вы зажжёте в первую очередь?',
'Может ли страус назвать себя птицей?' ]
ANSWERS = ['Сухих', 'Обед и ужин', 'Спичку', 'Нет']
key = random.randint(0,4)
attempts = 3
print('Загадка: ', RIDDLES[key])
while attempts != 0:
    answer = input('Ваш ответ: ')
    if answer == ANSWERS[key]:
       print('Верно! Молодец!')
       break 
    else:
       attempts -= 1
       print('Неверно! Осталось попыток: ', attempts)
```


