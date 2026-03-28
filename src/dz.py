for i in range(7):
    # ИНДЕКС ИДЁТ С 0 !!!
    if i == 0 or i == 6:   # Первая и последняя строка
        print('*' * 7)
    elif i == 1 or i == 5:  # 2 и 6 строка
        line = ''  # cтрока
        for j in range(7):
            if j == 1 or j == 5:   #2 и 6 место в строке
                line += '*'
            else:
                line += ' '
        print(line)
    elif i == 2 or i == 4:   # 3 и 5 строка
        line = ''
        for j in range(7):
            if j == 2 or j == 4:   # 3 и 5 место в строке
                line += '*'
            else:
                line += ' '
        print(line)
    else:  # i == 3
        line = ' ' * 3 + '*'  # 4 место в строке
        print(line)





print(' **   **')
print('**** ****')
print('*********')
for i in range(4):
    spaces_before = ' ' * (i + 1)
    stars = '*' * (7 - 2 * i)
    print(spaces_before + stars)