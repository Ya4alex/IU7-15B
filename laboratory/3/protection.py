import math as m

x1, y1 = map(float, input('1 (x y): ').split())
x2, y2 = map(float, input('2 (x y): ').split())
x3, y3 = map(float, input('3 (x y): ').split())

a1 = m.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
a2 = m.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
a3 = m.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if a1 < a2 and a1 < a3:
    m = 0.5 * m.sqrt(2 * a2 ** 2 + 2 * a3 ** 2 - a1 ** 2)
elif a2 < a1 and a2 < a3:
    m = 0.5 * m.sqrt(2 * a3 ** 2 + 2 * a3 ** 2 - a2 ** 2)
else:
    m = 0.5 * m.sqrt(2 * a2 ** 2 + 2 * a1 ** 2 - a3 ** 2)

print(f"Медиана из большего угла: {m:.7g}")
