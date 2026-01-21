#schurnal = {
#    'Чунгеевич': [2, 2, 2, 2, 2],
#    'Нублинов': [4, 4, 5],
#    'Ботаников': [5, 5, 4, 5, 2]
#}
#print(schurnal)

file = open('klassniy_schurnal.txt', 'r', encoding = 'utf-8')
text = file.read()[0:-1]
file.close()
linyi = text.split('\n')
print(linyi)

schurnal = {}
for l in linyi:
    F, O = l.split(':')
    ozenki = []
    for i in O:
        if i != ' ':
            ozenki.append(int(i))
    schurnal[F] = ozenki
            
while True:
    mod = int(input('1 - показать оценки, 2 - добавить оценку, 3 - добавить ученика, 4 - удалить ученика,5 - Показать среднюю оценку, 6 - показать всех, 7 - выход \n'))
    if mod == 1:
        F = input('Введите Фамилию:   ')
        if F in schurnal:
            print(schurnal[F])
        else: 
            print('Такого человека нет')
    elif mod == 2:
        F = input('Введите Фамилию:   ')
        if F in schurnal:
            mark = int(input('Введите оценку:  '))
            schurnal[F].append(mark)
        else: 
            print('Такого человека нет')
    elif mod == 3:
        F = input('Введите Фамилию:   ')
        if F not in schurnal:
            schurnal[F] = []
        else:
            print('Этот ученик уже есть в списке.')
    elif mod == 4:
        F = input('Введите Фамилию:    ')
        if F in schurnal:
            schurnal.pop(F)
        else:
            print('Этого ученика нет в списке')
    elif mod == 5:
        F = input('Введите Фамилию:    ')
        if F in schurnal:
            print(round(sum(schurnal[F]) / len(schurnal[F]), 2))
        # summ = 0
        # if F in schurnal:
        #     for i in schurnal[F]:
        #         summ += i
        #     srednya = summ / len(schurnal[F]) * 100
        #     srednya = int(srednya) / 100
        #     print(srednya)
        else:
            print('Этого ученика нет в списке')
    elif mod == 6:
        num = 0
        for key in schurnal:
            num += 1
            print(f'{num}. {key} : {schurnal[key]}')
            
    elif mod == 7:
        file = open('klassniy_schurnal.txt', 'w', encoding = 'utf-8')
        # КОГДА ФАЙЛ ОТКРЫВАЕТСЯ НА ЗАПИСЬ ОН ОЧИЩАЕТСЯ
        for key in schurnal:
            file.write(key + ':')
            for mark in schurnal[key]:
                file.write(' ' + str(mark))
            file.write('\n')
        file.close()
        break
            
