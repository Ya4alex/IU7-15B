# Яночкин Александр ИУ7-15Б
# Бабочка

x, y = map(float, input("Введите координаты точки через пробел: ").split())

# поскольку график симметричен относительно oY мы будем считать для правой части и сверять знак x
is_right, x = x >= 0, abs(x)

if (  # Верхнее крыло
        (1 <= x <= 9 and y <= -1 / 8 * (x - 9) ** 2 + 8) and  # 3 графика с проверками
        (x < 8 or y >= 7 * (x - 8) ** 2 + 1) and
        (x > 8 or y >= 1 / 49 * (x - 1) ** 2)
):
    if is_right:  # проверка на правое / левое крыло
        print("точка лежит в верхнем правом крыле")
    else:
        print("точка лежит в верхнем левом крыле")

elif (  # Нижнее крыло
        (1 <= x <= 8 and y <= -4 / 49 * (x - 1) ** 2) and
        (x < 2 or y >= 1 / 3 * (x - 5) ** 2 - 7) and
        (x > 2 or y >= -2 * (x - 1) ** 2 - 2)
):
    if is_right:  # проверка на правое / левое крыло
        print("точка лежит в нижнем правом крыле")
    else:
        print("точка лежит в нижнем левом крыле")
elif 0 <= x <= 1 and -4 * x ** 2 + 2 >= y >= 4 * x ** 2 - 6:  # тельце
    print("точка лежит в тельце")
elif y == 1.5 * x + 2:
    if is_right:  # проверка на правое / левое крыло
        print("точка лежит в правом усе")
    else:
        print("точка лежит в левом усе")
else:
    print("точка не лежит на бабочке")