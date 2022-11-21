# Яночкин Александр ИУ7-15Б
"""
Дана матрица символов. Заменить в ней все гласные английские буквы на
точки. Напечатать матрицу до и после преобразования.
"""

GL_en = set('eyuioa')

"""INPUT"""
# D----------------------
Hd, Wd = map(int, input("Введите размеры матрицы, высоту и ширину: ").split())
while Hd < 0 or Wd < 0:
    print("Некорректное значение")
    H, W = map(int, input("Введите размеры матрицы, высоту и ширину: ").split())

"""
d = [[]] * Hd
for i in range(Hd):
    x = input(f'Вводите элементы {i + 1} строки через пробел:\n').split()
    if len(x) != Wd and any(map(lambda x: len(x) == 1, x)):
        print(f"В строке должно быть {Wd} символов, написанных через пробел")
        x = input(f'Вводите элементы {i + 1} строки через пробел:\n').split()
    a[i] = x
"""

d = [[]] * Hd
for i in range(Hd):
    d[i] = [''] * Wd
    for j in range(Wd):
        [print(' o ' * j + ' # ' * int(i == ih) + ' o ' * (Wd - j - int(i == ih))) for ih in range(Hd)]
        x = input(f'Вводите элемент [{i + 1}:{j + 1}]: ')
        while len(x) != 1:
            print('Должен быть введён 1 символ!')
            x = input(f'Вводите элемент [{i + 1}:{j + 1}]: ')
        d[i][j] = x
"""END INPUT"""

for i, s in enumerate(d):
    for j, v in enumerate(s):
        d[i][j] = "".join(map(lambda x: '.' if x in GL_en else x, v))

print('\nD:')
for i in range(Hd):
    print(*[f"{j:<2}" for j in d[i]])

