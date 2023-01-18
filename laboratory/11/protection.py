import random


def get_random():
    return [random.randint(10, 100) for i in range(random.randint(10, 100))]


def check(m_s, m):
    return list(sorted(m)) == m_s


def test():
    for i in range(10000):
        m = get_random()
        m_s = comb_sort(m.copy())
        if not check(m_s, m):
            print(m)
            print(m_s)


def comb_sort(m: list, n: int = None):
    """
    Сортировка расческой
    :param m: массив
    :param n: длинна массива
    :return:
    """
    n = len(m)
    step = n
    flag = True
    while step > 1 or flag:
        if step > 1:
            step = int(step / 1.247)
        flag = False
        i = 0
        while i + step < n:
            if m[i] > m[i + step]:
                m[i], m[i + step] = m[i + step], m[i]
                flag = True
            i += step
    return m


def main():
    m = []
    while not m:
        try:
            m = list(map(int, input("Введите массив:\n").split()))
        except:
            print('Некорректное значение!')

    m = comb_sort(m)
    print('Отсортированный массив:')
    print(*m)


if __name__ == '__main__':
    # test()
    main()
