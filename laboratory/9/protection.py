"""
Найти столбцы с макс и минимальным эл
перемножить поэлементно столбцы -> список -> Q
Поменять на столбец Q все столбцы изначальной матрицы, где сред арифм < средн арифм в Q
"""

ex_d = [[0, 22, 31, 12],
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

# END INPUT
SR = [0] * Wd
i_max = i_min = None
v_max = v_min = None
for j in range(Wd):
    l_min = l_max = None
    sm = 0
    for i in range(Hd):
        if l_min is None or d[i][j] < l_min:
            l_min = d[i][j]
        if l_max is None or d[i][j] > l_max:
            l_max = d[i][j]
        sm += d[i][j]
    SR[j] = sm / Hd
    if v_min is None or l_min < v_min:
        v_min = l_min
        i_min = j
    if v_max is None or l_max > v_max:
        v_max = l_max
        i_max = j

Q = [d[i][i_max] * d[i][i_min] for i in range(Hd)]
print(f"min stolb: {i_min + 1}\nmax stolb: {i_max + 1}")
print('Q:')
print(*Q)
Qsr = sum(Q) / Hd

for j, sr in enumerate(SR):
    if sr >= Qsr:
        continue
    for i in range(Hd):
        d[i][j] = Q[i]


print('\nD:')
for i in range(Hd):
    print(*[f"{j:<6}" for j in d[i]])
