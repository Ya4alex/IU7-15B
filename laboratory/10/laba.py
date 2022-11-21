# Яночкин Александр ИУ7-15Б
# Интегралы

import math as ma
from functools import lru_cache

EPS = 1e-5
MAX_ITERATION = int(500)
TEST = {
    '1': (
        lambda x: 2 * ma.cos(x) + 3,
        lambda x: 2 * ma.sin(x) + 3 * x),
    '2': (
        lambda x: x ** 5,
        lambda x: x ** 6 / 6),
    '3': (
        lambda x: 1 / x,
        lambda x: ma.log(abs(x))),
    '4': (
        lambda x: 4,
        lambda x: 4 * x),
    '5': (
        lambda x: ma.sin(x),
        lambda x: - ma.cos(x))
}
func, p_func = TEST['5']


def method_0(m: tuple, p_f=p_func) -> float:
    """
    Метод рассчитывающий интеграл по первообразной
    :param m: [start:end]
    :param p_f: - функция для интегрирования
    :return:
    """
    try:
        return p_f(m[1]) - p_f(m[0])
    except:
        pass


@lru_cache(maxsize=100000)
def method_1(m: tuple, n, f=func) -> float:
    """
    Метод правых прямоугольников
    :param m: [start:end]
    :param n: - количество разбиений
    :param f: - функция для интегрирования
    :return:
    """
    try:
        d = (m[1] - m[0]) / n
        s = 0
        for i in range(n):
            s += f(m[0] + d * i)
        s *= d
        return s
    except:
        pass


@lru_cache(maxsize=100000)
def method_2(m: tuple, n, f=func) -> float:
    """
    Метод трапеций
    :param m: [start:end]
    :param n: - количество разбиений
    :param f: - функция для интегрирования
    :return:
    """
    try:
        d = (m[1] - m[0]) / n
        s = 0
        for i in range(1, n - 1):
            s += f(m[0] + d * i)
        s = d * ((f(m[0]) + f(m[1])) / 2 + s)
        return s
    except:
        pass


def method_3(m: tuple, n, f=func) -> float:
    """
    Метод Средних прямоугольников
    :param m: [start:end]
    :param n: - количество разбиений
    :param f: - функция для интегрирования
    :return:
    """
    try:
        d = (m[1] - m[0]) / n
        s = 0
        for i in range(1, n - 1):
            s += f(m[0] + d * i)
        s = d * ((f(m[0]) + f(m[1])) / 2 + s)
        return s
    except:
        pass


def part2_count_iterations(m: tuple, method_i: int):
    """
    Расчет для второй части программы
    :param m:
    :param method_i:
    :return:
    """
    print(f"\nРасчёт 𝑁 для метода {method_i + 1} по формуле:\n|𝐼(𝑁) − 𝐼(2𝑁)| < ε")
    method = METHOD_LIST[method_i]
    count_n = None
    eps = get_input(float, 'Введите точность ε: ', default=EPS)
    last = method(m, 1)
    for n in range(1, MAX_ITERATION):
        now = method(m, 2 ** n)
        t = abs(last - now)
        if t < eps:
            count_n = 2 ** (n - 1)
            break
        last = now
    if count_n is None:
        print(f'Не удалось достичь заданной точности за {MAX_ITERATION} итераций.')
    else:
        print(f"Количество участков разбиения (𝑁) для метода {method_i + 1} (при ε = {eps:.5g}):  {count_n}")


def get_input(data_type=float, text='Вводите значения: ', default=None, none=False):
    """
    Берет значение из ввода указанного типа данных и соответсвующее валидации
    :param data_type: тип данных
    :param text: Приглашение для ввода
    :param default: значение по умолчанию
    :param none: может ли быть None
    :return:
    """
    while True:
        x = input(text)
        if not x and (none or default is not None):
            if none:
                return None
            return default
        try:
            return data_type(x)
        except:
            print('Некорректное значение')


def get_input_from_string(data_type=float, count: int = None, text='Вводите значения: ', f=None) -> tuple:
    """
    Берет значения из строки через пробел и делает проверку по типу данных и количеству
    :param data_type: тип данных
    :param count: количество значений
    :param text: Текст приглашения ввода
    :param f: булева функция для валидации
    :return: кортеж с значениями
    """
    while True:
        a = input(text).split()
        if count is not None and len(a) != count:
            print(f'Вы должны ввести {count} значений!')
            continue
        try:
            ret = tuple(map(data_type, a))
            if f is None or all(map(f, ret)):
                return ret
        except ValueError:
            pass
        print(f"Введенные значения не соответствуют типу {data_type} или не проходят валидацию!")


def print_result_table(result):
    print('╔═══════════╦═══════════════╦═══════════════╗')
    print('║           ║       N1      ║       N2      ║')
    print('╠═══════════╬═══════════════╬═══════════════╣')
    for m_i in range(len(METHOD_LIST)):
        print(f'║{f"Метод {m_i + 1}":^11}║{norm(result[m_i][0]["res"])}║{norm(result[m_i][1]["res"])}║')
        if m_i != len(METHOD_LIST) - 1:
            print('╠═══════════╬═══════════════╬═══════════════╣')
    print('╚═══════════╩═══════════════╩═══════════════╝')


def print_result_table_plus(res):
    print('╔════════════════════════╦═══════════════╦═══════════════╗')
    print('║                        ║       N1      ║       N2      ║')
    print('╠═════════╦══════════════╬═══════════════╬═══════════════╣')
    for m_i in range(len(METHOD_LIST)):
        print(
            f'║{"":9}║{"Результат:":^14}║{norm(res[m_i][0]["res"])}║{norm(res[m_i][1]["res"])}║\n'
            f'║{f"Метод {m_i + 1}":^9}║{"Абсолют пог:":^14}║{norm(res[m_i][0]["abp"])}║{norm(res[m_i][1]["abp"])}║\n'
            f'║{"":9}║{"Относит пог:":^14}║{norm(res[m_i][0]["otp"])}║{norm(res[m_i][1]["otp"])}║'
        )
        if m_i != len(METHOD_LIST) - 1:
            print('╠═════════╬══════════════╬═══════════════╬═══════════════╣')
    print('╚═════════╩══════════════╩═══════════════╩═══════════════╝')


def norm(x: float, ln=15):
    if x is None or isinstance(x, str):
        return f"{str(x):^{ln}}"
    return f"{x:^+{ln}.{ln - 7 if abs(x) >= 1e7 or abs(x) <= 1e-2 else ln - 5}g}"


METHOD_LIST = (method_3,)


def main():
    m = get_input_from_string(float, count=2, text='Введите границы отрезка через пробел: ')
    while m[0] > m[1]:
        print('Некорректные значения, левая граница должна быть меньше правой!')
        m = get_input_from_string(float, count=2, text='Введите границы отрезка через пробел: ')
    n12 = get_input_from_string(int, count=2, text='Введите количество участков разбиения n1 n2: ', f=lambda x: x > 0)

    res = (
        ({}, {}),
        ({}, {}),
    )
    for method_i, method in enumerate((method_1, method_2)):
        for n_i, n in enumerate(n12):
            res[method_i][n_i]['res'] = method(m, n)
            if res[method_i][n_i]['res'] is None:
                print(f'Функция не непрерывна на [{m[0]:+.5g}:{m[1]:+.5g}]')
                return main()

    result_0 = method_0(m)
    print(f"Интеграл через первообразную: {norm(result_0)}")

    best_m_i = None
    best_pog = 0
    for m_i in (0, 1):
        for n_i in (0, 1):
            res[m_i][n_i]['abp'] = abs(res[m_i][n_i]['res'] - result_0)
            if result_0:
                res[m_i][n_i]['otp'] = abs(res[m_i][n_i]['abp'] / result_0 * 100)
            else:
                res[m_i][n_i]['otp'] = None
            if best_m_i is None or best_pog > res[m_i][n_i]['abp']:
                best_m_i = m_i
                best_pog = res[m_i][n_i]['abp']
    print_result_table_plus(res)
    return None
    # print(f"Наиболее точный метод: {best_m_i + 1}")
    #
    # part2_count_iterations(m, abs(best_m_i - 1))


if __name__ == "__main__":
    main()
