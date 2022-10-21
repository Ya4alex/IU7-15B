# Яночкин Александр ИУ7-15Б
# 1-B

n = int(input("Введите количество элементов списка: "))
while n < 0:
    print("Некорректное значение")
    n = int(input("Введите количество элементов списка: "))

a = [0] * n
if n:  # на случай если список пустой
    print('Вводите элементы:')
for i in range(n):
    a[i] = int(input(f"{i}: "))
# -

nx = int(input("Введите индекс элемента: "))
while not (0 <= nx <= n):
    print("Индекс не попадает в область!")
    nx = int(input("Введите индекс элемента: "))

x = int(input("Введите элемент: "))

a.append(0)
old = a[nx]
a[nx] = x
for i in range(nx + 1, n + 1):
    old, a[i] = a[i], old

# -
print(*a)  # выводим
