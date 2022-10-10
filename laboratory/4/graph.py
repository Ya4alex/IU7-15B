# Яночкин Александр ИУ7-15Б
# выбрал 2 функцию
import math as m

WIDTH = 200  # Ширина отображаемого графика в кол. символов

print('Диапазон X\n(пустой ввод - значение по умолчанию)')  # ввод данных. Пустой ввод - значение по умолчанию
x0 = float(input('Введите начальное значение\t(по умолчанию -0.6)\tx0 = ') or -0.6)
h = float(input('Введите шаг значений\t\t(по умолчанию 0.04)\t h = ') or 0.04)
xn = float(input('Введите конечное значение\t(по умолчанию 0.4)\txn = ') or 0.4)

RUN = True

if not h:  # проверка на нулевой шаг
    print('Шаг не может равняться 0')
    RUN = False
    count_x = 0
    # тут нужен был sys.exit()
else:
    count_x = int((xn - x0) / h + 1)
if RUN and count_x <= 0:  # проверка на наличие x
    print('В указанный промежуток не попало ни одно значение')
    RUN = False
    # тут нужен был sys.exit()

y_min = None  # минимальное значение функции 2
y_max = None  # Максимальное значение функции 2
x_max_dop = y_max_dop = None  # для решения дополнительной задачи

# ТАБЛИЦА
if RUN:
    print('╔═══════════╦═══════════╦═══════════╗')
    print('║     x     ║     y1    ║     y2    ║')
    print('╠═══════════╬═══════════╬═══════════╣')

    for i in range(count_x):  # +1 так как в примере xn включительно
        x = x0 + h * i  # нахождение x
        y1 = m.pow(m.e, -x) + m.pow(x, 2) - 2  # f1()
        y2 = m.pow(x, 3) - 19.7 * m.pow(x, 2) + 28.9 * x + 5.62  # f2()

        print(f'║{x:^+11.{5 if abs(x) >= 1e7 or abs(x) <= 1e-2 else 7}g}'
              f'║{y1:^+11.{5 if abs(y1) >= 1e7 or abs(y1) <= 1e-2 else 7}g}'
              f'║{y2:^+11.{5 if abs(y2) >= 1e7 or abs(y2) <= 1e-2 else 7}g}║')  # заполнение таблицы значениями

        if y_min is None or y2 < y_min:  # нахождение минимума
            y_min = y2
        if y_max is None or y2 > y_max:  # нахождение максимума
            y_max = y2
        if y_max_dop is None or y1 > y_max_dop:
            y_max_dop = y1
            x_max_dop = x

    print('╚═══════════╩═══════════╩═══════════╝')
    print(f"Максимальное значение\ta1: {y_max_dop:+.8g}\n\t\tдостигается при  x: {x_max_dop:+.8g}\n")

# ГРАФИК:
    # служебные переменные
    d_range = y_max - y_min  # область значений f2()
    if not d_range:  # проверка на возможность построения графика по условию
        print('Невозможно построить график, нужно хотя бы 2 значения x')
        # тут нужен был sys.exit()
    else:
        f = WIDTH / d_range  # соотношение ширины в символах и области значения (коэффициент)
        posX0 = int(-y_min * f)  # символьная координата абсциссы

# ЗАСЕЧКИ
        # расчет расположения засечек
        z = int(input('Введите количество засечек (4-8) (по умолчанию 8): ') or 8)
        z_step = WIDTH // z  # шаг в символах
        z_value_step = (d_range - (WIDTH % z) * f) / z  # шаг в значениях
        z_value = y_min + 0.5 / f + z_value_step / f / 2  # первоначальное значение
        # 0.5 / f нужно, чтобы брать значение для z_value из "центра" знакоместа

        print(f"График y2(x):\n═══════════╦" + '═' * (z_step // 2), end='')
        for i in range(z):
            # подстановка координат. 12 - ширина 1 засечки в символах
            # заполнение идет справа символом "═"
            modification = 5 if abs(z_value) > 1e7 or abs(z_value) <= 1e-2 else 7  # расчет формата для красивого вывода
            print(f"╤{z_value:═<+11.{modification}g}", end='')
            if i != z - 1:
                print('═' * (z_step - 12), end='')

            z_value += z_value_step  # увеличиваем счетчик на шаг значения
        print('═' * (WIDTH % z + z_step - z_step // 2 - 11) + '╗')

# ТОЧКИ
        for i in range(count_x):  # то же, что и в таблице
            x = x0 + h * i  # расчет аргумента
            y2 = m.pow(x, 3) - 19.7 * m.pow(x, 2) + 28.9 * x + 5.62  # расчет значения f2(x)

            pos = int((y2 - y_min) * f)  # позиция "*" в символах
            if 0 < posX0 < pos != pos:  # 3 варианта расположения точки и абсциссы
                if posX0 < pos:  # абсцисса точка
                    s = ' ' * posX0 + '│' + ' ' * (pos - posX0 - 1) + '*' + ' ' * (WIDTH - pos)
                else:  # точка абсцисса
                    s = ' ' * pos + '*' + ' ' * (posX0 - pos - 1) + '│' + ' ' * (WIDTH - posX0)
            else:  # точка (абсцисса не попадает в видимую часть графика
                s = ' ' * pos + '*' + ' ' * (WIDTH - pos)

            modification = 5 if abs(x) >= 1e7 or abs(x) <= 1e-2 else 7  # расчет формата для красивого вывода
            print(f"{x:^+11.{modification}g}╟{s}║")  # подстановка

        print('═══════════╩' + '═' * (WIDTH + 1) + '╝')
