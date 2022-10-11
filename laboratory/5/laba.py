# Яночкин Александр ИУ7-15Б
# Вариант: 30
"""
    В моём варианте при аргументе |x| > 1, последовательность "скачет" вокруг 0, в конечном счете удаляясь от него,
то есть является расходящейся. Поэтому для таких x сумму ряда вычислить невозможно, соответственно нельзя вычислить и
точность.
Я разделил все аргументы x на |x| > 1 и |x| <= 1.
    Для |x| <= 1 возможно найти сумму с точностью e.
    Для |x| > 1  возможно найти сумму по i-ый член последовательности с точностью e.
Сайт, где можно проверить последовательность:
https://www.kontrolnaya-rabota.ru/s/ryad/summa/?infinity=0&nm=&function=%28-1%29%5E%28n+-+1%29%28%28%280.1%29%5En%29%29%2Fn&N=n&n0=1
"""
import math as m

x = float(input('Введите значение аргумента (0.5): ') or 0.5)
e = float(input('Введите точность (1e-5): ') or 1e-5)
while e <= 0:  # я взял просто модуль от е, но мне сказали, что так нельзя, нужно дать пользователю по рукам
    e = float(input('Точность не может быть отрицательной!\nВведите точность (1e-5): ') or 1e-5)
maxi = int(input('Введите максимальное количество итераций (32): ') or 32)
h = float(input('Введите шаг (1): ') or 1)

IS_CONV: bool = abs(x) <= 1  # {сходящаяся: True ,расходящаяся: False} последовательность
if IS_CONV:
    print('\nРяд сходящийся, вычислить точность возможно.')
else:
    print(f"Ряд расходящийся, вычислить точность невозможно.\nБудет посчитана сумма ряда по {maxi} член")

print('╔════════════╦════════════════╦════════════════╗')
print('║ № итерации ║        t       ║        s       ║')
print('╠════════════╬════════════════╬════════════════╣')

e_success = False  # флаг, удалось ли достичь указанной точности
s: float = 0  # сумма
ot: float = 0  # переменная с значением предыдущего члена (изначально 0)
i: int = 1  # номер итерации, если maxi = 0, то i в циклу for не будет создан - создаем вручную
ei: float = m.inf  # текущая точность
for i in range(1, maxi + 1):
    t = m.pow(-1, i - 1) * m.pow(x, i) / i  # получение значения текущего члена
    ei = abs(abs(ot) - abs(t))  # вычисление текущей точности
    s += t  # увеличиваем сумму на текущий член
    if not (i - 1) % h:  # простая проверка шага печати
        print(f'║{i:^12.6g}'
              f'║{t:^+16.{9 if abs(t) >= 1e7 or abs(t) <= 1e-2 else 12}g}'
              f'║{s:^+16.{9 if abs(s) >= 1e7 or abs(s) <= 1e-2 else 12}g}║')  # заполнение таблицы значениями
    if IS_CONV and ei <= e:  # проверка достижения указанной точности при сходящейся последовательности
        e_success = True  # переключение флага о достижении указанной точности
        break
    ot = t  # запись текущего значение члена в предыдущий для следующей итерации
print('╚════════════╩════════════════╩════════════════╝')

if e_success:  # если удалось достичь заданной точности
    print(f"Сумма бесконечного ряда: {s:+.10g} с точностью e: {e:+.10g} за {i} итераций")
elif not IS_CONV:  # если последовательность расходящаяся
    print(f"Сумма ряда по {i} член: {s:+.12}")  # формально нужно вывести "итераций недостаточно"
else:  # если не удалось достичь точности и последовательность сходящаяся
    print(
        f"Количество итераций ({maxi}) не хватило, для вычисления суммы с точностью {e:+.10g}\n"
        f"Сумма бесконечного ряда: {s:+.10g} с точностью e: {ei:+.10g}"  # формально эту строку не нужно выводить
    )
