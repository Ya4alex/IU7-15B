# Яночкин Александр ИУ7-15Б
"""
метод вставок с бинарным поиском
"""
import random

from laboratory import module
from laboratory.module import norm

DEFAULT_MASS = [9, 7, 2, 4, 1, 6]


def get_true_sort(mass):
    return list(sorted(mass))


def gen_rand_list(n: int, sort=False, reverse=False, ran=(1, 999)) -> list:
    """
    Возвращает случайный список длиной n
    :param n: длинна списка
    :param sort: сортировать
    :param reverse: в обратном порядке
    :param ran: диапазон значений [a, b]
    :return:
    """
    mass = [random.randint(*ran) for i in range(n)]
    if sort or reverse:
        return list(sorted(mass, reverse=reverse))
    return mass


@module.time_of_function
def custom_sort(mass: list, n: int = None) -> (list, int):
    """
    Сортировка методом бинарных вставок
    :param mass: Массив для сортировки
    :param n: длинна массива
    :return: массив, количество перестановок, время выполнения
    """
    n = n or len(mass)
    p_count = 0
    for i in range(n):
        value = mass[i]
        left, right = 0, i - 1
        while left <= right:  # бинарный поиск
            middle = (right + left) // 2
            if value >= mass[middle]:
                left = middle + 1
            else:
                right = middle - 1
        for j in range(i, left, -1):  # перестановки
            mass[j] = mass[j - 1]
            p_count += 1
        mass[left] = value
    return mass, p_count


def create_table():
    return [
        '╔════════════════════════',
        '║                        ',
        '╠════════════════════════',
        '║ t-время p-перестановки ',
        '╠═■═■═■═■═■═■═■═■═■═■═■═■',
        '║ Упорядоченный список   ',
        '╠════════════════════════',
        '║ Случайный список       ',
        '╠════════════════════════',
        '║ Упоряд. в обратном пор.',
        '╚════════════════════════',
    ]


def add_column(table, column):
    if len(column) != len(table):
        raise ValueError('Колонка не соответствует таблице')
    for i, v in enumerate(column):
        table[i] += v
    return table


def close_table(table):
    column = ('╗', '║', '╣', '║', '╣', '║', '╣', '║', '╣', '║', '╝',)
    return add_column(table, column)


def print_table(table):
    [print(i) for i in table]


def iter_for_mass(table, n):
    missives = [gen_rand_list(n, sort=True), gen_rand_list(n), gen_rand_list(n, reverse=True)]
    res = [(), (), ()]
    for i, mass in enumerate(missives):
        res[i] = custom_sort(mass)
    column = (
        f"╦═══════════════════",
        f"║{n:^+19}",
        f"╬═══════════╤═══════",
        f"║     t     │   p   ",
        f"╬═■═■═■═■═■═╪═■═■═■═",
        f"║{norm(res[0][2], 11)}│{norm(res[0][1], 7)}",
        f"╬═══════════╪═══════",
        f"║{norm(res[1][2], 11)}│{norm(res[1][1], 7)}",
        f"╬═══════════╪═══════",
        f"║{norm(res[2][2], 11)}│{norm(res[2][1], 7)}",
        f"╩═══════════╧═══════",
    )
    table = add_column(table, column)

    return table


def main():
    test = list(module.get_input_from_string(int, text='Введите массив:\n', default=DEFAULT_MASS))
    print(f"отсортированный массив средствами Python:")
    print(*get_true_sort(test))
    # my sort
    print(f"отсортированный массив методом бинарных вставок:")
    print(*custom_sort(test)[0])

    N = list(module.get_input_from_string(
        int,
        count=3,
        text='Введите длинны массивов N1 N2 N3:\n',
        f=lambda x: x >= 0,
        default=(5, 6, 7)
    ))
    table = create_table()
    for n in N:
        table = iter_for_mass(table, n)
    table = close_table(table)
    print_table(table)


if __name__ == "__main__":
    main()
