# Яночкин Александр ИУ7-15Б
# 4
import math as m

# ввод
n = int(input("Введите количество элементов списка: "))
while n <= 0:
    print("Некорректное значение")
    n = int(input("Введите количество элементов списка: "))

a = [0] * n
print('Вводите элементы:')
for i in range(n):
    a[i] = int(input(f"{i}: "))
# ---

delta = 0  # сдвиг за счет insert
for i in range(n):
    if 2 > a[i + delta]:  # убираем отрицательные и 0, 1
        a[i + delta] = 0
        continue
    for j in range(2, int(m.sqrt(a[i + delta])) + 1):  # проверка на простоту
        if a[i + delta] % j == 0:
            a[i + delta] = 0
            continue  # не простое - уходим
    if i > 0 and a[i + delta] <= a[i - 1 + delta]:  # ограничиваем последовательности подходящие под условие
        a.insert(i + delta, 0)
        delta += 1  # сдвигаем

a = [0] + a + [0]  # окружаем защитными 0
s = 0
res = (0, 0)  # хранение индексов для среза
for i in range(n + 2):
    if not a[i]:
        if i - s > res[1] - res[0]:
            res = s, i
        s = i
result = a[res[0] + 1: res[1]]
if result:
    print("Максимальная возрастающая последовательность простых чисел:")
    print(*result)
else:
    print("Ни одной последовательности не найдено.")
