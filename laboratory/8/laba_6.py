# Яночкин Александр ИУ7-15Б
"""
6. Выполнить транспонирование квадратной матрицы.
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

for i in range(H):
    for j in range(i + 1, H):
        a[i][j], a[j][i] = a[j][i], a[i][j]

for i in range(H):
    print(*[f"{j:<6}" for j in a[i]])
