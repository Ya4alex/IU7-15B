# y = -x^2 + 9
import math as m

WIDTH = 120

x0 = float(input('x0: ') or -6)
h = float(input(' h: ') or 0.4)
xn = float(input('xn: ') or 6)

x_count = int((xn - x0) // h + 1)
y_min = None
y_max = None

print('-------------------------')
print('|     x     |     y     |')
print('|-----------------------|')
for i in range(x_count):
    x = x0 + h * i
    y = - m.pow(x, 2) + 9

    print(
        f"|{x:^+11.{5 if abs(x) >= 1e7 or abs(x) <= 1e-2 else 7}g}"
        f"|{y:^+11.{5 if abs(y) >= 1e7 or abs(y) <= 1e-2 else 7}g}|"
    )
    if y_min is None or y < y_min:
        y_min = y
    if y_max is None or y > y_max:
        y_max = y

print('-------------------------')
d_range = y_max - y_min
f = WIDTH / d_range
posOX = int(-y_min * f)

print(
    '-' * 11 + f"|{y_min:-<+11.{5 if abs(y_min) >= 1e7 or abs(y_min) <= 1e-2 else 7}g}" + '-' * (WIDTH - 21) +
    f"{y_max:->+11.{5 if abs(y_max) >= 1e7 or abs(y_max) <= 1e-2 else 7}g}"
)

for i in range(x_count):
    x = x0 + h * i
    y = - m.pow(x, 2) + 9

    pos = int((y - y_min) * f)
    if 0 <= posOX != pos:
        if posOX < pos:
            s = ' ' * posOX + '|' + ' ' * (pos - posOX - 1) + '*' + ' ' * (WIDTH - pos)
        else:
            s = ' ' * pos + '*' + ' ' * (posOX - pos - 1) + '|' + ' ' * (WIDTH - posOX)
    else:
        s = ' ' * pos + '*' + ' ' * (WIDTH - pos)
    print(f"{x:^+11.{5 if abs(x) >= 1e7 or abs(x) <= 1e-2 else 7}g}|{s}")
