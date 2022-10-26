# Яночкин Александр ИУ7-15Б
# 6. Замена двух подряд идущих цифр на последнюю цифру их суммы

n = int(input("Введите количество элементов списка: "))
while n < 0:
    print("Некорректное значение")
    n = int(input("Введите количество элементов списка: "))

a = [''] * n
if n:  # на случай если список пустой
    print('Вводите элементы:')
for i in range(n):
    a[i] = input(f"{i}: ")

for i in range(n):
    x = a[i]
    nx = len(x)
    if nx < 2:
        continue
    ret = ''

    j = 0
    while j < nx:
        if j < nx - 1 and x[j].isdigit() and x[j + 1].isdigit():
            ret += str((int(x[j + 1]) + int(x[j])) % 10)
            j += 1
        else:
            ret += x[j]
        j += 1

    a[i] = ret

print(*a or '∅')  # выводим
