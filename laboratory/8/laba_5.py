# Яночкин Александр ИУ7-15Б
"""
5. Найти максимальное значение в квадратной матрице над главной диагональю и
минимальное - под побочной диагональю.
"""

H = int(input("Введите размер матрицы: "))
while H <= 0 or H <= 0:
    print("Некорректное значение")
    H = int(input("Введите размер матрицы: "))

a = [[]] * H

for i in range(H):
    x = list(map(int, input(f'Вводите элементы {i + 1} строки через пробел:\n').split()))
    if len(x) != H:
        print(f"В строке должно быть {H} элементов")
        x = list(map(int, input(f'Вводите элементы {i + 1} строки через пробел:\n').split()))
    a[i] = x

k_min = k_max = None
for i in range(H - 1):
    kmi = min(a[i][i + 1:])
    kma = max(a[i + 1][:i + 1])
    if k_min is None or k_min > kmi:
        k_min = kmi
    if k_max is None or k_max < kma:
        k_max = kma

if k_min is None or k_max is None:
    print("Не удалось выполнить в заданной матрице")
else:
    print(f"Минимальное:  {k_min}\nМаксимальное: {k_max}")
