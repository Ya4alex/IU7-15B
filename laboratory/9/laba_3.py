# Яночкин Александр ИУ7-15Б
"""
Подсчитать в каждой строке матрицы D количество элементов, превышающих
суммы элементов соответствующих строк матрицы Z. Разместить эти
количества в массиве G, умножить матрицу D на максимальный элемент
массива G. Напечатать матрицу Z, матрицу D до и после преобразования, а
также массив G.
"""

ex_d = [[1, 22, 31],
        [4, 5, 6]]

ex_z = [[1, 2],
        [3, 4],
        [5, 6],
        [7, 8]]

"""INPUT"""
# D----------------------
Hd, Wd = map(int, input("Введите размеры матрицы, высоту и ширину: ").split())
while Hd < 0 or Wd < 0:
    print("Некорректное значение")
    H, W = map(int, input("Введите размеры матрицы, высоту и ширину: ").split())

d = [[]] * Hd
for i in range(Hd):
    x = list(map(float, input(f'Вводите элементы {i + 1} строки через пробел:\n').split()))
    if len(x) != Wd:
        print(f"В строке должно быть {Wd} элементов")
        x = list(map(float, input(f'Вводите элементы {i + 1} строки через пробел:\n').split()))
    d[i] = x
if Hd == Wd == 0:
    d = ex_d
    Hd, Wd = len(d), len(d[0])

# Z----------------------
Hz, Wz = map(int, input("Введите размеры матрицы, высоту и ширину: ").split())
while Hz < 0 or Wz < 0:
    print("Некорректное значение")
    H, W = map(int, input("Введите размеры матрицы, высоту и ширину: ").split())

z = [[]] * Hz
for i in range(Hz):
    x = list(map(float, input(f'Вводите элементы {i + 1} строки через пробел:\n').split()))
    if len(x) != Wz:
        print(f"В строке должно быть {Wz} элементов")
        x = list(map(float, input(f'Вводите элементы {i + 1} строки через пробел:\n').split()))
    z[i] = x
if Hz == Wz == 0:
    z = ex_z
    Hz, Wz = len(z), len(z[0])

# G----------------------
g = [0] * Hd

"""END INPUT"""
for si in range(Hd):
    sm = k = 0
    for i in z[si]:  # ????? sum(z[si])
        sm += i

    for el in d[si]:  # подсчёт
        k += 1 if el > sm else 0
    g[si] = k

mg = None  # max(g) # ???????????
for i in g:
    if mg is None or mg > i:
        mg = i

for i in range(Hd):
    for j in range(Wd):
        d[i][j] *= mg

print('\nZ:')
for i in range(Hz):
    print(*[f"{j:<6}" for j in z[i]])

print('\nD:')
for i in range(Hd):
    print(*[f"{j:<6}" for j in d[i]])

print('\nG:\n', *g)
