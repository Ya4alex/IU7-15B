# Яночкин Александр ИУ7-15Б
"""
Сформировать матрицу C путём построчного перемножения матриц A и B
одинаковой размерности (элементы в i-й строке матрицы A умножаются на
соответствующие элементы в i-й строке матрицы B), потом сложить все
элементы в столбцах матрицы C и записать их в массив V. Напечатать матрицы
A, B, C и массив V.
"""

ex_a = [[1, 22, 31],
        [4, 5, 6],
        [4, 5, 6]]

ex_b = [[1, 2, 5],
        [3, 4, 8],
        [5, 6, 1]]

"""INPUT"""
# A----------------------
H, W = map(int, input("Введите размеры матрицы, высоту и ширину: ").split())
while H < 0 or W < 0:
    print("Некорректное значение")
    H, W = map(int, input("Введите размеры матрицы, высоту и ширину: ").split())

a = [[]] * H
for i in range(H):
    x = list(map(float, input(f'Вводите элементы {i + 1} строки через пробел:\n').split()))
    if len(x) != W:
        print(f"В строке должно быть {W} элементов")
        x = list(map(float, input(f'Вводите элементы {i + 1} строки через пробел:\n').split()))
    a[i] = x
if H == W == 0:
    a = ex_a
    H, W = len(a), len(a[0])

# B----------------------
b = [[]] * H
for i in range(H):
    x = list(map(float, input(f'Вводите элементы {i + 1} строки через пробел:\n').split()))
    if len(x) != W:
        print(f"В строке должно быть {W} элементов")
        x = list(map(float, input(f'Вводите элементы {i + 1} строки через пробел:\n').split()))
    b[i] = x
if H == W == 0:
    b = ex_b
    H, W = len(b), len(b[0])
# C----------------------
c = [[]] * H
# V----------------------
v = [0] * W
"""END INPUT"""

for i in range(H):
    c[i] = [None] * W
    for j in range(W):
        c[i][j] = a[i][j] * b[i][j]

for j in range(W):
    s = 0
    for i in range(H):
        s += c[i][j]
    v[j] = s

print('\nA:')
for i in range(H):
    print(*[f"{j:<6}" for j in a[i]])

print('\nB:')
for i in range(H):
    print(*[f"{j:<6}" for j in b[i]])

print('\nC:')
for i in range(H):
    print(*[f"{j:<6}" for j in c[i]])

print('\nV:\n', *v)
