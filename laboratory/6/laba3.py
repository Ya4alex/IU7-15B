# Яночкин Александр ИУ7-15Б
# 3

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

x = int(input("Введите номер экстремума: "))
while x <= 0:
    print("Некорректное значение")
    x = int(input("Введите номер экстремума: "))

e = None
k = 0  # счетчик экстремума
for i in range(1, n - 1):
    if a[i - 1] > a[i] < a[i + 1] or a[i - 1] < a[i] > a[i + 1]:
        e = a[i]
        k += 1
    if k == x:  # уходим, если нашли
        break

if k == x:
    print(f"{e} - экстремум №{x}")
else:
    print('Не найден экстремум с таким номером.')
