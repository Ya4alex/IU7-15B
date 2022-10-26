# Яночкин Александр ИУ7-15Б
# 3. Нечётные элементы

a = list(map(int, input('Введите элементы массива через пробел:\n').split()))
n = len(a)

set_i = 0
for i in range(n):
    if not a[i] % 2:
        a[set_i] = a[i]
        set_i += 1

print(*a[:set_i] or '∅')  # выводим
