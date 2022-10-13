import math as m
# Все то же самое, только проще последовательность
# (1 / 3) ** n / n!
e = abs(float(input('Точность (1e-10): ') or 1e-10))
maxi = int(float(input('Интервал (64): ') or 64))
h = int(float(input('Шаг (1): ') or 1))

is_done = False
s = 0
i = 0
print('╔════════════╦════════════════╦════════════════╗')
print('║ № итерации ║        t       ║        s       ║')
print('╠════════════╬════════════════╬════════════════╣')
for i in range(1, maxi + 1):
    t = m.pow(1 / 3, i) / m.factorial(i)
    s += t
    if not (i + 1) % h:
        print(f'║{i:^12.6g}'
              f'║{t:^+16.{9 if abs(t) >= 1e7 or abs(t) <= 1e-2 else 12}g}'
              f'║{s:^+16.{9 if abs(s) >= 1e7 or abs(s) <= 1e-2 else 12}g}║')
    if t <= e:
        is_done = True
        break
print('╚════════════╩════════════════╩════════════════╝')

if is_done:
    print(f"Сумма: {s:.15g} с точностью: {e:.15g} за {i} итераций.")
else:
    print(f"Не удалось достигнуть точности {e:.15g} за {maxi} итераций.")
