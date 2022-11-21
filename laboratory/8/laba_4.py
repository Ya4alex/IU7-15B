# Яночкин Александр ИУ7-15Б
"""
Переставить местами столбцы с максимальной и минимальной суммой элементов.
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
for i in range(W):
    k = sum([s[i] for s in a])
    if k_min is None or k_min > k:
        i_min, k_min = i, k
    if k_max is None or k_max < k:
        i_max, k_max = i, k

if k_min is None or k_max is None:
    print("В матрице не нашлось столбов по условию")
else:
    for i in range(H):
        a[i][i_min], a[i][i_max] = a[i][i_max], a[i][i_min]

for i in range(H):
    print(*[f"{j:<6}" for j in a[i]])
