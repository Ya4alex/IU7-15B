# Яночкин Александр ИУ7-15Б
# 1. Поиск элемента с наибольшим числом английских гласных букв

LITERS = set('eyuioa')

n = int(input("Введите количество элементов списка: "))
while n < 0:
    print("Некорректное значение")
    n = int(input("Введите количество элементов списка: "))

a = [''] * n
if n:  # на случай если список пустой
    print('Вводите элементы:')
for i in range(n):
    a[i] = input(f"{i}: ")

k_max = -1
ret = 0
for i in a:
    k = 0
    for j in i:
        if j.lower() in LITERS:
            k += 1
    if k > k_max:
        k_max = k
        ret = i

print(ret or '∅')  # выводим
