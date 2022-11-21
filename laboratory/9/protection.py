ex_d = [[1, 22, 31, 12],
        [4, 5, 16, 1],
        [42, 15, 6, 50]]

"""INPUT"""
# D----------------------
Hd, Wd = map(int, input("Введите размеры матрицы, высоту и ширину: ").split())
while Hd < 0 or Wd < 0:
    print("Некорректное значение")
    H, W = map(int, input("Введите размеры матрицы, высоту и ширину: ").split())

d = [[]] * Hd
for i in range(Hd):
    x = list(map(int, input(f'Вводите элементы {i + 1} строки через пробел:\n').split()))
    if len(x) != Wd:
        print(f"В строке должно быть {Wd} элементов")
        x = list(map(int, input(f'Вводите элементы {i + 1} строки через пробел:\n').split()))
    d[i] = x
if Hd == Wd == 0:
    d = ex_d
    Hd, Wd = len(d), len(d[0])

for i in range(Hd // 2 + Hd % 2):
    for j in range(i + 1, Wd // 2 + Wd % 2):
        d[i][j], d[Hd - i - 1][Wd - j - 1] = d[Hd - i - 1][Wd - j - 1], d[i][j]

print('\nD:')
for i in range(Hd):
    print(*[f"{j:<6}" for j in d[i]])
