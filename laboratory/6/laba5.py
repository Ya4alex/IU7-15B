# Яночкин Александр ИУ7-15Б
# 5

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

minim = maxim = None  # индексы

for i in range(n):
    if a[i] > 0:
        if minim is None or a[minim] > a[i]:  # поиск
            minim = i
        if maxim is None or a[maxim] < a[i]:
            maxim = i

if maxim is None or minim is None:  # если не нашли
    print("Невозможно определить минимальный и/или максимальный элемент в данной последовательности согласно условию.")
else:
    a[minim], a[maxim] = a[maxim], a[minim]  # замена
    print(*a)
