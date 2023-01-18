# ИУ7-15Б Яночкин Александр
from random import randint, choice

GL = 'eyuioa'
SGL = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'ch', 'sh']
COUNTRIES = ['ru', 'uk', 'usa', 'fr', 'bg', 'au', 'pl', 'gr', 'rm']
STRUCT = {
    'name': 'Список людей',
    'struct': {
        'id': int,
        'first_name': str,
        'last_name': str,
        'sex': str,
        'price': int,
        'age': int,
        'country': str,
    },
    'pos': ['id', 'first_name', 'last_name', 'sex', 'price', 'age', 'country'],
    's_field_1': 'first_name',
    's_field_2': ('sex', 'country'),
}


def form(x):
    return f"{x:^13}" if len(x) < 13 else f"{x[:10]:10}..."


def generate_random_line():
    gen_name = lambda: (choice(SGL) * randint(0, 1) + "".join(
        [choice((GL, SGL)[i % 2]) for i in range(randint(5, 7))])).capitalize()
    return {
        'id': randint(100000, 999999),
        'first_name': gen_name(),
        'last_name': gen_name(),
        'sex': choice(('m', 'w')),
        'price': randint(100, 10000),
        'age': randint(1, 100),
        'country': choice(COUNTRIES),
    }


def write_file(path: str, n=30):
    try:
        with open(path, 'w') as f:
            for i in range(n):
                line = generate_random_line()
                s = ",".join([str(line[j]) for j in STRUCT['pos']]) + '\n'
                f.write(s)
    except:
        print('Ошибка при записи файла!')


def print_file(path: str):
    try:
        with open(path, 'r') as f:
            print('╔═════════════╦═════════════╦═════════════╦═════════════╦═════════════╦═════════════╦═════════════╗')
            print('║      id     ║   f_name    ║    l_name   ║     sex     ║    price    ║     age     ║  country    ║')
            print('╠═════════════╬═════════════╬═════════════╬═════════════╬═════════════╬═════════════╬═════════════╣')
            line = f.readline()
            if not line:
                print('Файл пуст')
            while line:
                values = line.strip().split(',')
                if len(values) != len(STRUCT['pos']):
                    print('Строка:')
                    print(*values)
                    print('Не соответствует заданной структуре!')
                    return
                line = '║'.join(list(map(lambda x: form(x), values)))
                print(f"║{line}║")
                line = f.readline()
            print('╚═════════════╩═════════════╩═════════════╩═════════════╩═════════════╩═════════════╩═════════════╝')
    except Exception as e:
        print('Файл не найден или изменён.')


def add_row(path):
    row = [''] * len(STRUCT['pos'])
    for i, field in enumerate(STRUCT['pos']):
        value = input(f'Введите {field}:')
        while True:
            try:
                STRUCT['struct'][field](value)
                break
            except:
                print('Некорректное значение!')
                value = input(f'Введите {field}: ')
        row[i] = value
    try:
        with open(path, 'a') as f:
            f.write(",".join(row) + '\n')
    except:
        print('Ошибка при записи файла!')


def search_1(path):
    s = input('Введите страну: ')
    while not s:
        s = input('Введите страну: ')
    res = []
    try:
        with open(path, 'r') as f:
            line = f.readline()
            if not line:
                print('Файл пуст')
            while line:
                values = line.strip().split(',')
                if len(values) != len(STRUCT['pos']):
                    print('Строка:')
                    print(*values)
                    print('Не соответствует заданной структуре!')
                    return
                if values[6] == s:
                    line = '║'.join(list(map(lambda x: form(x), values)))
                    res.append(f"║{line}║")
                line = f.readline()
    except Exception as e:
        print('Файл не найден или изменён.')
    if not res:
        return print('Ничего не найдено')
    print('Все результаты по запросу:')
    print('╔═════════════╦═════════════╦═════════════╦═════════════╦═════════════╦═════════════╦═════════════╗')
    print('║      id     ║   f_name    ║    l_name   ║     sex     ║    price    ║     age     ║  country    ║')
    print('╠═════════════╬═════════════╬═════════════╬═════════════╬═════════════╬═════════════╬═════════════╣')
    for s in res:
        print(s)
    print('╚═════════════╩═════════════╩═════════════╩═════════════╩═════════════╩═════════════╩═════════════╝')


def search_2(path):
    print('-Поиск по имени и фамилии:')
    s = input('Введите имя: ').strip()
    while not s:
        s = input('Введите имя: ').strip()
    s2 = input('Введите фамилию: ').strip()
    while not s:
        s2 = input('Введите фамилию: ').strip()
    res = []
    try:
        with open(path, 'r') as f:
            line = f.readline()
            if not line:
                print('Файл пуст')
            while line:
                values = line.strip().split(',')
                if len(values) != len(STRUCT['pos']):
                    print('Строка:')
                    print(*values)
                    print('Не соответствует заданной структуре!')
                    return
                if s in values[1] or s2 in values[2]:
                    line = '║'.join(list(map(lambda x: form(x), values)))
                    res.append(f"║{line}║")
                line = f.readline()
    except Exception as e:
        print('Файл не найден или изменён.')
    if not res:
        return print('Ничего не найдено')
    print('Все результаты по запросу:')
    print('╔═════════════╦═════════════╦═════════════╦═════════════╦═════════════╦═════════════╦═════════════╗')
    print('║      id     ║   f_name    ║    l_name   ║     sex     ║    price    ║     age     ║  country    ║')
    print('╠═════════════╬═════════════╬═════════════╬═════════════╬═════════════╬═════════════╬═════════════╣')
    for s in res:
        print(s)
    print('╚═════════════╩═════════════╩═════════════╩═════════════╩═════════════╩═════════════╩═════════════╝')


FUNCS = {
    '1': (True, '\t1. Выбрать файл для работы'),
    '2': (write_file, '\t2. Инициализировать базу данных'),
    '3': (print_file, '\t3. Вывести содержимое базы данных'),
    '4': (add_row, '\t4. Добавить запись в конец базы данных'),
    '5': (search_1, '\t5. Поиск по одному полю'),
    '6': (search_2, '\t6. Поиск по двум полям'),
    'exit': (None, '\texit. Выйти.')
}


def main():
    path = None
    while True:
        print('══════════════════════════════════════════')
        print(*map(lambda x: x[1], FUNCS.values()), sep='\n')
        print('══════════════════════════════════════════')
        mode = input("mode: ")
        while mode not in FUNCS.keys():
            print('Нет такого действия')
            mode = input("mode: ")
        f = FUNCS[mode][0]
        if f is None:
            break
        if f is True:
            path = input('Введите путь ("file.csv"): ') or 'file.csv'
            print()
            continue
        if path is None:
            print('\nВыберите файл (1)\n')
            continue
        f(path)
        print('')


if __name__ == '__main__':
    main()
