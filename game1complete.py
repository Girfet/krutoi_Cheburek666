import random


# Константы
MAX_ATTEMPTS = 3

RIDDLES_DATA = [
    {'question': 'Каких камней нет в море?', 'answer': 'Сухих'},
    {'question': 'Что нельзя съесть на завтрак?', 'answer': 'Обед и ужин'},
    {'question': 'У вас есть только одна спичка. В тёмной комнате стоят керосиновая лампа, печь и свеча. Что вы зажжёте в первую очередь?', 'answer': 'Спичку'},
    {'question': 'Может ли страус назвать себя птицей?', 'answer': 'Нет'}
]


def main():
    """Главная функция игры 'Угадай загадку'."""
    print('Добро пожаловать в игру "Угадай загадку"!')
    
    # Выбираем случайную загадку
    key = random.randrange(len(RIDDLES_DATA))
    riddle = RIDDLES_DATA[key]
    
    print(f'Загадка: {riddle["question"]}')
    
    # Даём пользователю несколько попыток
    for attempt in range(MAX_ATTEMPTS):
        answer = input('Ваш ответ: ')
        
        # Проверяем ответ (игнорируем регистр и пробелы)
        if answer.strip().lower() == riddle['answer'].lower():
            used_attempts = attempt + 1
            print(f'Верно! Молодец! Вы угадали с {used_attempts}-й попытки!')
            break
    else:
        # Этот блок выполнится, если цикл завершился без break
        print(f'Игра окончена! Правильный ответ: {riddle["answer"]}')


if __name__ == '__main__':
    main()
