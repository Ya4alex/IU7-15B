# delete word
def delete_word(text):
    to_replace = input('Введите слово, которое необходимо удалить: ')
    if not to_replace == '':
        if (len(to_replace.split())) != 1:
            print('При таком вводе учитывается только первое слово.')
            word = to_replace.split()[0]
    for idx, sentence in enumerate(text):
        text[idx] = " ".join(
            [word for word in sentence.split(" ") if word != to_replace]
        )

def just_alpha(s):
    a = s.split()

# replace word
def replace_word(text):
    to_replace = input('Введите слово, которое необходимо заменить: ')
    while to_replace == '':
        print('Нельзя заменить пустую строку')
        to_replace = input('Введите слово, которое необходимо заменить: ')

    if (len(to_replace.split())) != 1:
        print('При таком вводе заменится только первое слово.')
        word = to_replace.split()[0]

    replace_with = input('Введите слово, на которое необходимо заменить: ')

    while replace_with == '':
        print('Нельзя заменить пустую строку')
        replace_with = input('Введите слово, которое необходимо заменить: ')

    if (len(replace_with.split())) != 1:
        print('При таком вводе учитывается только первое слово.')
        new_word = replace_with.split()[0]
    for idx, sentence in enumerate(text):
        text[idx] = " ".join(
            [
                word if word != to_replace else replace_with
                for word in sentence.split(" ")
            ]
        )