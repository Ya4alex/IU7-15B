# Яночкин Александр ИУ7-15Б
"""
Найти столбец, имеющий определённое свойство по варианту
2. Наименьшее количество отрицательных элементов.
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

s_min = None
k_min = None
for i in range(W):
    s = [s[i] for s in a]
    k = 0
    for j in s:
        if j < 0:
            k += 1
    if k_min is None or k_min > k:
        k_min, s_min = k, s

if s_min:
    [print(i) for i in s_min]
    map(print, s_min)
else:
    print("В матрице не нашлось столбов по условию")
