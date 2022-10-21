# Яночкин Александр ИУ7-15Б
# 2-B

n = int(input("Введите количество элементов списка: "))
while n <= 0:
    print("Некорректное значение")
    n = int(input("Введите количество элементов списка: "))

a = [0] * n
print('Вводите элементы:')
for i in range(n):
    a[i] = int(input(f"{i}: "))
# -

nx = int(input("Введите индекс элемента: "))
while not (0 <= nx < n):
    print("Индекс не попадает в область!")
    nx = int(input("Введите индекс элемента: "))

b = [0] * (n - 1)  # создаем копию
delta = 0  # сдвиг
for i in range(n):
    if i == nx:
        delta += 1
        continue
    b[i - delta] = a[i]  # смещаем

# -
if b:  # выводим
    print(*b)
else:
    print("В списке не осталось элементов")

