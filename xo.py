import os
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
# создание поля
field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
simvol = YELLOW + 'x' + LIGHT_GREEN
# Вывод правил игры
turn = 0

#вывод поля
print(f'{LIGHT_GREEN}   1  2  3 ')
print(f'A [{field[0][0]}][{field[0][1]}][{field[0][2]}]')
print(f'B [{field[1][0]}][{field[1][1]}][{field[1][2]}]')
print(f'C [{field[2][0]}][{field[2][1]}][{field[2][2]}]')

while True:
    # Игра
    
    print(f'ход {simvol}')
    move = input('Введите координаты клетки (например A1): ').upper()
    # проверка на ошибку
    if len(move) != 2:
        print('Должно быть 2 символа')
        continue
    if move[1] not in '123':
        print('Во втором значении должна быть цифра 1-3')
        continue
    if move[0] not in 'ABC':
        print('В первом значении должны быть буквы ABC')
        continue
    stolb_num = int(move[1]) - 1

    if move[0] == 'A':
        ryad_num = 0
    elif move[0] == 'B':
        ryad_num = 1
    elif move[0] == 'C':
        ryad_num = 2
    #проверка на занятость клетки
    if field[ryad_num][stolb_num] != ' ':
        print('Эта клетка уже занята')
        continue
    
    field[ryad_num][stolb_num] = simvol 
    
    #очистка поля
    os.system('CLS')
    # проверка на победу  
    if (field[ryad_num][0] == field[ryad_num][1] == field[ryad_num][2] or 
      field[0][stolb_num] == field[1][stolb_num] == field[2][stolb_num] or
      (field[0][0] == field[1][1] == field[2][2] or
      field[0][2] == field[1][1] == field[2][0]) and field[1][1] != ' '):
        print('   1  2  3 ')
        print(f'A [{field[0][0]}][{field[0][1]}][{field[0][2]}]')
        print(f'B [{field[1][0]}][{field[1][1]}][{field[1][2]}]')
        print(f'C [{field[2][0]}][{field[2][1]}][{field[2][2]}]')

        print(f'Победа {simvol}')
        break
    # проверка на ничью
    turn += 1
    if turn == 9:
        print('   1  2  3 ')
        print(f'A [{field[0][0]}][{field[0][1]}][{field[0][2]}]')
        print(f'B [{field[1][0]}][{field[1][1]}][{field[1][2]}]')
        print(f'C [{field[2][0]}][{field[2][1]}][{field[2][2]}]')

        print('ничья')
        break
    # конец хода
    if simvol == YELLOW + 'x' + LIGHT_GREEN :
        simvol = LIGHT_BLUE + 'o' + LIGHT_GREEN
    else:
        simvol = YELLOW + 'x' + LIGHT_GREEN
    print('   1  2  3 ')
    print(f'A [{field[0][0]}][{field[0][1]}][{field[0][2]}]')
    print(f'B [{field[1][0]}][{field[1][1]}][{field[1][2]}]')
    print(f'C [{field[2][0]}][{field[2][1]}][{field[2][2]}]')
    