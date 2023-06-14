import copy

print("          '''Добро пожаловать в игру Крестики-Нолики''' \n"
      "  '''Перед вами игровое поле 3х3 с нумерацией линий и столбцов'''\n"
      "'''Игроки вводят поочередно координаты своего хода из терминала'''")

start_field = [                 # Создаем стартовый шаблон игрового поля
    [' ', 1, 2, 3],
    [1, '-', '-', '-'],
    [2, '-', '-', '-'],
    [3, '-', '-', '-'],
]


def output(field):              # Функция вывода игрового поля в терминал
    for i in field:
        for j in i:
            print(j, end=' ')
        print()


play_field = copy.deepcopy(start_field)      # Копируем шаблон в список Игрового поля
output(play_field)                           # и выводим его в терминал


def move():                                     # Функция поочередной ввода координат хода
    while True:                                 # с проверкой корректности ввода
        a = int(input("Введите номер линии: "))
        if a < 1 or a > 3:
            print("Неверный ввод!")
            continue
        break
    while True:
        b = int(input("Введите номер столбца: "))
        if b < 1 or b > 3:
            print("Неверный ввод!")
            continue
        break
    return a, b


def move_x():                                # функция хода Крестиков
    print("'''  Ходят крестики!  '''")
    while True:
        a, b = move()
        if play_field[a][b] == '-':          # проверка на возможность хода
            play_field[a][b] = 'X'           # вносим изменение в игровое поле
            break
        else:
            print("Сделать ход нельзя. Поле уже занято!")
            continue


def move_0():                                # функция хода Ноликов
    print("'''  Ходят нолики!  '''")
    while True:
        a, b = move()
        if play_field[a][b] == '-':          # проверка на возможность хода
            play_field[a][b] = '0'           # вносим изменение в игровое поле
            break
        else:
            print("Сделать ход нельзя. Поле уже занято!")
            continue


def combinations():              # Формирование списка combi, в который вносятся в виде строк
    combi = []                   # все возможные комбинации линий, столбцов и диагоналей
    list_play = play_field.copy()

    for i in range(1, 4):        # Внесение в спискок combi строк,
        line = ''                # состоящих из значений каждой отдельной линии
        for j in range(1, 4):
            line += list_play[i][j]
        combi.append(line)

    for j in range(1, 4):        # Внесение в спискок combi строк,
        column = ''              # состоящих из значений каждого отдельного столбца
        for i in range(1, 4):
            column += list_play[i][j]
        combi.append(column)

    diag_1 = ''                  # Внесение в список combi значений
    diag_2 = ''                  # обеих диагоналей
    for i in range(1, 4):
        for j in range(1, 4):
            if i == j:
                diag_1 += list_play[i][j]
            if i + j == 4:
                diag_2 += list_play[i][j]
    combi.append(diag_1)
    combi.append(diag_2)
    return combi


def check_win():                              # Функция проверки списка комбинаций на совпадение
    for combi in combinations():              # с выиграшной комбинацией
        if combi == 'XXX':
            print("Крестики победили!")
            return True
        elif combi == '000':
            print("Нолики победили!")
            return True


y_n = input("Хотите сыграть? y/n: ")          # Основное тело программы
yes = y_n == 'y'                              # Спрашиваем, хочет ли игрок сыграть
count_x = 0                                   # Создаем счетчики побед Крестиков и Ноликов
count_0 = 0
while yes:                                    # Начало бесконечного цикла игр
    count_move = 0                            # Счетчик ходов
    while count_move < 10:                    # Цикл попарных ходов крестиков и ноликов
        move_x()                              # Ход Крестиков
        count_move += 1
        output(play_field)                    # Вывод игрового поля с учетом сделанного хода
        if count_move > 4 and check_win():    # Проверка выиграшных комбинаций начиная с
            count_x += 1                      # пятого хода
            break

        if count_move == 9:                          # Если были сделаны все ходы, и победитель
            print("Что ж, и такое бывает. Ничья!")   # не определился,то Ничья
            break

        move_0()                              # Ход Ноликов
        count_move += 1
        output(play_field)                    # Вывод игрового поля с учетом сделанного хода
        if count_move > 5 and check_win():
            count_0 += 1
            break

    print(f"Итоговый счёт  <<<Крестики {count_x} : {count_0} Нолики>>>")  # Вывод счёта побед
    y_n = input("Хотите сыграть еще раз? y/n: ")                          # Запрос на новую игру
    yes = y_n == 'y'
    if not yes:
        print("Игра окончена.")
        break
    play_field = copy.deepcopy(start_field)         # Сброс игрового поля и
    output(play_field)                              # вывод его в терминал
