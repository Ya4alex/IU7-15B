# Яночкин Александр ИУ?-15Б
"""
Поиск эл в списке строк
с наибольшим кол согласных (англ) и нечетным кол гласных
"""

GL = set(list("eyuioa"))  # можно переписать сразу в сет, но это долго)
SG = set(list("qwrtpsdfghjklzxcvbnm"))

n = int(input("Введите кол элементов: "))
while n <= 0:
    print("Некорректное значение")
    n = int(input("Введите кол элементов: "))

a = [''] * n
for i in range(n):
    a[i] = input(f"Вводите {i + 1} строку:\n")

sg_max = None
ret = ""
for s in a:
    sg_c = gl_c = 0
    for i in s.lower():
        if i in GL:
            gl_c += 1
        elif i in SG:
            sg_c += 1
    if gl_c % 2 == 1 and (sg_max is None or sg_c > sg_max):
        sg_max, ret = sg_c, s

if sg_max is None:
    print("Не удалось найти подходящую строку")
else:
    print('Строка по условию:', ret, sep='\n')
