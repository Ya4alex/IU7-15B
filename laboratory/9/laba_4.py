# Яночкин Александр ИУ7-15Б
"""
Задана матрица D и массив I, содержащий номера строк, для которых
необходимо определить максимальный элемент. Значения максимальных
элементов запомнить в массиве R. Определить среднее арифметическое
вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
среднее арифметическое значение.
"""

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

# I----------------------
while True:
    i_mas = list(map(lambda x: int(x) - 1, input('Вводите массив I:\n').split()))
    if all(map(lambda x: 0 <= x < Hd, i_mas)):
        break
    print("Введённые значения не могут быть номерами строк массива D!")

r = [0] * len(i_mas)
"""END INPUT"""

print(r)

for i, search_i in enumerate(i_mas):
    r[i] = max(d[search_i])

print('\nD:')
for i in range(Hd):
    print(*[f"{j:<6}" for j in d[i]])

print('\nI:\n', *map(lambda x: x + 1, i_mas))
print('\nR:\n', *r)
print(f"\nСреднее значение:\n{sum(r) / len(r):g}")  # подсчёт среднего
