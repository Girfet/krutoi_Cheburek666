import random

RIDDLES_DATA = [
  {'question': 'Каких камней нет в море?', 'answer': 'Сухих'}, 
  {'question': 'Что нельзя съесть на завтрак?', 'answer': 'Обед и ужин'},
  {'question': 'У вас есть только одна спичка. В тёмной комнате стоят керосиновая лампа, '
   'печь и свеча. Что вы зажжёте в первую очередь?', 'answer': 'Спичку'},
  {'question': 'Может ли страус назвать себя птицей?', 'answer': 'Нет'} 
]
MAX_ATTEMPTS = 3

def main():
   print('Добро пожаловать в игру "Угадай загадку"!')

   key = random.randint(0, len(RIDDLES_DATA) - 1)

   print('Загадка: ', RIDDLES_DATA[key])

# TODO: Можно использовать более питонический подход: for _ in range(attempts)
# TODO: Добавить обработку регистра: answer.strip().lower() == ANSWERS[key].lower()
   while attempts != 0:
      answer = input('Ваш ответ: ')
      if answer == ANSWERS[key]:
       # TODO: Можно добавить сообщение о количестве использованных попыток
         print('Верно! Молодец!')
         break 
      else:
         attempts -= 1
       # TODO: Добавить проверку на attempts == 0 и вывести правильный ответ
       # TODO: Можно использовать f-строки: f'Неверно! Осталось попыток: {attempts}'
         print('Неверно! Осталось попыток: ', attempts)

# TODO: Добавить сообщение после цикла, если закончились попытки:
# if attempts == 0:
#     print(f'Игра окончена! Правильный ответ: {ANSWERS[key]}')

if __name__ == '__main__':
   main()