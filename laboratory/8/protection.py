"""
Целочисл мин макс
найти сумму элементов подматрицы образыва
"""

H, W = map(int, input("Введите размеры матрицы высоту и ширину: ").split())
while H <= 0 or W <= 0:
    print("Некорректное значение!")
    H, W = map(int, input("Введите размеры матрицы высоту и ширину: ").split())

a = [[]] * H

for i in range(H):
    x = list(map(int, input(f"Вводите элементы {i + 1} строки:\n").split()))
    while len(x) != W:
        print(f"В строке должно быть {W} элементов!")
        x = list(map(int, input(f"Вводите элементы {i + 1} строки:\n").split()))
    a[i] = x

v_min, pos_min = None, ()
v_max, pos_max = None, ()
for i, s in enumerate(a):
    for j, v in enumerate(s):
        if v_min is None or v < v_min:
            v_min, pos_min = v, (i, j)
        if v_max is None or v > v_max:
            v_max, pos_max = v, (i, j)
print(f"Минимальный:  {v_min}\n"
      f"Максимальный: {v_max}")

pos0 = min(pos_max[0], pos_min[0]), min(pos_max[1], pos_min[1])
pos1 = max(pos_max[0], pos_min[0]), max(pos_max[1], pos_min[1])

k = 0
for s in a[pos0[0]: pos1[0] + 1]:
    k += sum(s[pos0[1]: pos1[1] + 1])
    print(*s[pos0[1]: pos1[1] + 1])

print(f"Сумма элементов подматрицы: {k}")
