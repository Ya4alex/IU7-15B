# Яночкин Александр ИУ7-15Б
# 2. Чётные элементы

a = list(map(int, input('Введите элементы массива через пробел:\n').split()))

cnt = 0
for i in a:
    if not i % 2:
        cnt += 1

a = [0] * cnt + a

n = len(a)
set_i = 0
i = cnt
while i < n:
    a[set_i] = a[i]
    i += 1
    set_i += 1
    if not a[i - 1] % 2:
        a[set_i] = a[i - 1]
        set_i += 1

print(*a or '∅')  # выводим
