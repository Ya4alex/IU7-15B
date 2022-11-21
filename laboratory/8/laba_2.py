# Яночкин Александр ИУ7-15Б
"""
Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов.
"""

H, W = map(int, input("Введите размеры матрицы, высоту и ширину: ").split())
while H <= 0 or H <= 0:
    print("Некорректное значение")
    H, W = map(int, input("Введите размеры матрицы, высоту и ширину: ").split())

a = [[]] * H

for i in range(H):
    x = list(map(int, input(f'Вводите элементы {i + 1} строки через пробел:\n').split()))
    if len(x) != W:
        print(f"В строке должно быть {W} элементов")
        x = list(map(int, input(f'Вводите элементы {i + 1} строки через пробел:\n').split()))
    a[i] = x

i_min = i_max = None
k_min = k_max = None
for i, s in enumerate(a):
    k = len([j for j in s if j < 0])
    if k_min is None or k_min > k:
        i_min, k_min = i, k
    if k_max is None or k_max < k:
        i_max, k_max = i, k

if k_min is None or k_max is None:
    print("Не нашлось строк с отрицательными элементами")
else:
    a[i_min], a[i_max] = a[i_max], a[i_min]

for i in range(H):
    print(*[f"{j:<6}" for j in a[i]])
