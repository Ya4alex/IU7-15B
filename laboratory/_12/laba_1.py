# Яночкин Александр ИУ7-15Б
"""
1. Выровнять текст по левому краю.
2. Выровнять текст по правому краю.
3. Выровнять текст по ширине.
4. Удаление всех вхождений заданного слова.
5. Замена одного слова другим во всём тексте.
6. Вычисление арифметических выражений над целыми числами внутри текста (сложение и вычитание).
7. Найти (вывести на экран) и затем удалить слово или предложение по варианту.
        3. Предложение с максимальным количеством слов, начинающихся на заданную
        букву.
"""

OPERATORS = {
    '+': int.__add__,
    '-': int.__sub__,
}
SENTENCES_ENDS = '.!?'


def read_from_file(path: str):
    with open(path, 'r') as f:
        text = list(map(lambda x: x.strip(), f.readlines()))
    return text


def _format_center(st: str, n: int) -> str:
    lst = st.split()
    if len(lst) == 1:
        return f"{st.strip():^n}"
    p = n - sum(map(lambda x: len(x), lst))
    srp, osp = p // (len(lst) - 1), p % (len(lst) - 1)
    res = lst[0]

    for i, s in enumerate(lst[1:]):
        pr = srp + 1 if i < osp else srp
        res += ' ' * pr + s
    return res


def format_to_page(text: list[str], mode='<') -> list[str]:
    method = {
        '<': str.ljust,
        '>': str.rjust,
        '^': _format_center
    }.get(mode)
    if method is None:
        raise ValueError(f'Неправильный mode "{mode}"')
    max_str = max(map(lambda x: len(x), text))
    for i, s in enumerate(text):
        text[i] = method(" ".join(s.split()), max_str)
    return text


# Удаление всех вхождений заданного слова
def del_word(text: list[str]) -> list[str]:
    word = input('Введите слово, которое необходимо удалить: ')
    if not word == '':
        if (len(word.split())) != 1:
            print('При таком вводе учитывается только первое слово.')
            word = word.split()[0]
    for i in range(len(text)):
        text[i] = ' ' + text[i] + ' '
        for j in ' "(':
            for k in ' .,;:)!?"':
                if k != ' ':
                    text[i] = text[i].replace(j + word + k, j + k)
                    text[i] = text[i].replace(j + word.capitalize() + k, j + k)
                else:
                    text[i] = text[i].replace(j + word + k, j)
                    text[i] = text[i].replace(j + word.capitalize() + k, j)

        text[i] = text[i][1:-1]
    return text


# Замена одного слова другим во всём тексте
def replace_word(text):
    word = input('Введите слово, которое необходимо заменить: ')
    while word == '':
        print('Нельзя заменить пустую строку')
        word = input('Введите слово, которое необходимо заменить: ')

    if (len(word.split())) != 1:
        print('При таком вводе заменится только первое слово.')
        word = word.split()[0]
    new_word = input('Введите слово, на которое необходимо заменить: ')

    while new_word == '':
        print('Нельзя заменить пустую строку')
        new_word = input('Введите слово, на которое необходимо заменить: ')

    if (len(new_word.split())) != 1:
        print('При таком вводе учитывается только первое слово.')
        new_word = new_word.split()[0]
    for i in range(len(text)):
        if text[i] == word:
            text[i] = new_word
            continue
        text[i] = ' ' + text[i] + ' '
        for j in ' "(':
            for k in ' .,;:)!?"':
                text[i] = text[i].replace(j + word + k, j + new_word + k)
                text[i] = text[i].replace(j + word.capitalize() + k, j + new_word + k)
        text[i] = text[i][1:-1]
    return text


def _calc_str(s: str) -> list[tuple[str, str]]:
    ret = []
    i_s = 0
    flag_is_math = False
    flag_wait_operator = True
    flag_wait_digit = True
    i_last_math_char = 0
    for i, char in enumerate(s):
        if flag_is_math:
            if char.isdigit():
                if not flag_wait_digit:  # save and new
                    if i_s != i_last_math_char:
                        ret.append(((i_s, i_last_math_char + 1), s[i_s:i_last_math_char + 1]))
                    i_s = i
                    flag_wait_digit = True
                flag_wait_operator = True

                i_last_math_char = i
            elif char in OPERATORS.keys():
                if not flag_wait_operator:  # save and new
                    if i_s != i_last_math_char:
                        ret.append(((i_s, i_last_math_char + 1), s[i_s:i_last_math_char + 1]))
                    i_s = i
                else:
                    flag_wait_operator = False
                flag_wait_digit = True

                i_last_math_char = i
            elif char in " \t":
                flag_wait_digit = not flag_wait_operator
            else:
                flag_is_math = False
                flag_wait_operator = True
                if i_s != i_last_math_char:
                    ret.append(((i_s, i_last_math_char + 1), s[i_s:i_last_math_char + 1]))
        else:
            if char.isdigit() or char in OPERATORS.keys():
                flag_is_math = True
                i_s = i
                flag_wait_operator = char not in OPERATORS.keys()

                i_last_math_char = i
    if i_s != i_last_math_char:
        ret.append(((i_s, i_last_math_char + 1), s[i_s:i_last_math_char + 1]))
    ret = list(map(lambda x: (s[x[0][0]:x[0][1]], _calc_calc(x[1])), ret))
    return ret


def _calc_calc(s: str) -> str:
    for op in OPERATORS.keys():
        s = s.replace(op, f' {op} ')
    mas = s.split()
    sm = 0
    last_op = OPERATORS['+']
    for item in mas:
        if item.isdigit():
            sm = last_op(sm, int(item))
        elif item in OPERATORS.keys():
            last_op = OPERATORS[item]
        else:
            raise Exception('wtf')
    return str(sm)


def calc_text(text: list[str]) -> list[str]:
    for i, s in enumerate(text):
        for inert, new in _calc_str(s):
            text[i] = text[i].replace(inert, new)
    return text


def find_replace(text: list[str]) -> list[str]:
    find_char = input('Введите букву: ').strip().lower()
    while len(find_char) != 1:
        find_char = input('!Введите букву: ').strip().lower()

    i_sentences: list[tuple[tuple[int, int], tuple[int, int]]] = []
    start: tuple[int, int] = 0, 0
    find = True
    for i_s, s in enumerate(text):
        for i_char, char in enumerate(s):
            if not find and char not in '\t ':
                start = i_s, i_char
                find = True
            elif char in SENTENCES_ENDS:
                if text[start[0]][start[1]].lower() == find_char:
                    i_sentences.append((start, (i_s, i_char + 1)))
                find = False
    sentences = [''] * len(i_sentences)
    mx = 0
    mx_i = None
    for i, ((s_i_s, s_i_ch), (f_i_s, f_i_ch)) in enumerate(i_sentences):
        if s_i_s == f_i_s:
            st = text[s_i_s][s_i_ch:f_i_ch]
        else:
            st = text[s_i_s][s_i_ch:]
            for s in text[s_i_s + 1:f_i_s]:
                st += ' ' + s
            st += ' ' + text[f_i_s][:f_i_ch]
        if len(st.split()) > mx:
            mx = len(st.split())
            mx_i = i
        sentences[i] = st
    print(f'Предложение с максимальным количеством слов, начинающееся на букву {find_char}:')
    print(sentences[mx_i])
    (s_i_s, s_i_ch), (f_i_s, f_i_ch) = i_sentences[mx_i]
    text[s_i_s] = text[s_i_s][:s_i_ch]
    for i in range(f_i_s - s_i_s - 1):
        del text[s_i_s + 1]
    text[s_i_s + 1] = text[s_i_s + 1][f_i_ch:]

    return text


FUNCS = {
    '1': (lambda x: format_to_page(x, '<'), '1. Выровнять текст по левому краю.'),
    '2': (lambda x: format_to_page(x, '>'), '2. Выровнять текст по правому краю.'),
    '3': (lambda x: format_to_page(x, '^'), '3. Выровнять текст по ширине'),
    '4': (del_word, '4. Удаление всех вхождений заданного слова.'),
    '5': (replace_word, '5. Замена одного слова другим во всём тексте.'),
    '6': (calc_text, '6. Вычисление арифметических выражений над целыми числами внутри текста (+-).'),
    '7': (find_replace, '7. Найти (вывести на экран) и затем удалить Предложение с максимальным количеством слов,'
                        ' начинающихся на заданнуюбукву'),
    'exit': (None, 'exit. Выйти.')
}


def main():
    text = read_from_file('file.txt')
    while True:
        print(*text, sep='\n')
        print()
        print(*map(lambda x: x[1], FUNCS.values()), sep='\n')
        mode = input("mode: ")
        while mode not in FUNCS.keys():
            print('Нет такого действия')
            mode = input("mode: ")
        f = FUNCS[mode][0]
        if f is None:
            break
        text = f(text)


if __name__ == '__main__':
    main()
