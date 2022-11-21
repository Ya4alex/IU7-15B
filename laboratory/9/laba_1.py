# Яночкин Александр ИУ7-15Б
"""
Даны массивы D и F. Сформировать матрицу A по формуле
    ajk = sin(dj+fk).
Определить среднее арифметическое положительных чисел каждой строки
матрицы и количество элементов, меньших среднего арифметического.
Результаты записать соответственно в массивы AV и L. Напечатать матрицу A в
виде матрицы и рядом столбцы AV и L.
"""
import math as m

D = list(map(float, input("Введите значения массива D через пробел:\n").split()))
F = list(map(float, input("Введите значения массива F через пробел:\n").split()))
D_len = len(D)
F_len = len(F)

a = [[]] * D_len

AV = [0] * D_len
for j in range(D_len):
    a[j] = [0.] * F_len
    kol = 0
    for k in range(F_len):
        a[j][k] = m.sin(D[j] + F[k])
        if a[j][k] > 0:
            AV[j] += a[j][k]
            kol += 1
    if kol == 0:
        AV[j] = None
    else:
        AV[j] /= kol

L = [0] * D_len
for i, v in enumerate(a):
    if AV[i] is not None:
        L[i] = len(list(filter(lambda x: x < AV[i], v)))
    else:
        L[i] = None

for i in range(D_len):
    if AV[i] is not None and L[i] is not None:
        av = f"| {AV[i]:8^+.5g}".ljust(11)
        l = f"~ {L[i]}"
    else:
        av = '| None      ~ None'
        l = ''
    print(*[f"{j:8^+.5g}".ljust(11) for j in a[i]], av, l)
