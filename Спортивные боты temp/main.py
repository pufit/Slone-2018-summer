template = '''
|———|———|———|
| %s | %s | %s |
|———|———|———|
| %s | %s | %s |
|———|———|———|
| %s | %s | %s |
|———|———|———|
'''

field = [[' '] * 3, [' '] * 3, [' '] * 3]

print('Загрузка спортивного бота #1381')

print('Внимание! Этот бот попал под программу о защите\n'
      'интелектуальных способностей ИИ "Уступи боту первый ход".\n'
      'Бот всегда ходит первым')


def do_step(x, y, t):
    field[y - 1][x - 1] = t
    if field[y - 1] == ['x', 'x', 'x'] or field[x - 1] == ['x', 'x', 'x']:
        print('Бот выиграл!')
        exit()


def print_field():
    lst = []
    for i in range(3):
        lst += field[i]
    print()
    print(template % tuple(lst))


j = 1

while True:
    do_step(j, 1, 'x')
    print_field()
    a, b = list(map(int, input('Введите координаты клетки: ').split()))
    do_step(a, b, 'o')
    j += 1
    if j == 4:
        j = 1
