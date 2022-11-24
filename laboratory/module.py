import time


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
            print(f"Установлено значение по умолчанию: {default}")
            return default
        try:
            return data_type(x)
        except:
            print('Некорректное значение')


def get_input_from_string(
        data_type=float, count: int = None,
        text='Вводите значения: ', f=None,
        none=False,
        default=None,
) -> tuple:
    """
    Берет значения из строки через пробел и делает проверку по типу данных и количеству
    :param data_type: тип данных
    :param count: количество значений
    :param text: Текст приглашения ввода
    :param f: булева функция для валидации
    :param none: Может ли быть None
    :param default: Значение по умолчанию
    :return: кортеж с значениями
    """
    while True:
        a = input(text).split()
        if not a:
            if none:
                return
            elif default is not None:
                print(f"Установлено значение по умолчанию: {default}")
                return default
        elif count is not None and len(a) != count:
            print(f'Вы должны ввести {count} значений!')
            continue
        try:
            ret = tuple(map(data_type, a))
            if f is None or all(map(f, ret)):
                return ret
        except ValueError:
            pass
        print(f"Введенные значения не соответствуют типу {data_type} или не проходят валидацию!")


def norm(x: float, ln=15):
    if x is None or isinstance(x, str):
        return f"{str(x):^{ln}}"
    return f"{x:^+{ln}.{ln - 7 if abs(x) >= 1e7 or abs(x) <= 1e-2 else ln - 5}g}"


def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        ret_time = time.perf_counter_ns() - start_time
        return res + (ret_time,)

    return wrapped
