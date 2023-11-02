from random import choice

import click

import os
folder_name = 'dictionaries'
file_name = 'basic_list_of_words.txt'
FILE_PATH = os.path.abspath(f"{folder_name}/{file_name}")

# Импортирование библиотек

# ====================================================================================================================================================================================================================================================


@click.command()
@click.option('--password_num', '-pn', type=int, default=1, help='Count of password.', show_default=True)
@click.option('--word_num', '-wn', type=int, default=1, help='How many words in password.', show_default=True)
@click.option('--dictionary_of_words', '-df', type=str, multiple=True, help="", show_default=True)
@click.option('--separators', '-s', type=str, default='', help='Spaces in your password.', show_default=True)
@click.option('--change_symbols', '-ch', type=str, multiple=True, help="", show_default=True)
@click.option('--print_passwords', '-pp', help='', show_default=True, is_flag=True)
# ====================================================================================================================================================================================================================================================
def start_program(password_num, word_num, dictionary_of_words, separators, change_symbols, print_passwords):

    dictionary_of_words = get_dictionary_2_0(dictionary_of_words)
    change_symbols_from, change_symbols_to = get_replce_symbols(change_symbols)

    password_list = basic_passwords_list(
        password_num, word_num, dictionary_of_words)
    password_list = separators_and_new_password_list(separators, password_list)
    password_list = replace_symbols(
        change_symbols_from, change_symbols_to, password_list)
    password_print(password_list, print_passwords)


def basic_passwords_list(password_num, word_num, dictionary_of_words):
    passwords_list = []

    for i in range(password_num):
        words_list = []

        for l in range(word_num):
            words_list.append(choice(dictionary_of_words))

        passwords_list.append(words_list)

    return passwords_list

# ready


def get_dictionary_2_0(dictionary_of_words):
    if not (dictionary_of_words):
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            new_dictionary = f.read()
            new_dictionary = new_dictionary.split()

    else:
        new_dictionary = " ".join(dictionary_of_words)
        new_dictionary = new_dictionary.split()

    return new_dictionary

# ready


def separators_and_new_password_list(separators, password_list):

    new_password_list = []

    for i in password_list:
        modified_word = separators.join(list(i))
        new_password_list.append(modified_word)

    return new_password_list

# ready


def password_print(password_list, print_passwords):
    if not (print_passwords):
        with open('C:\\Users\\User\\PYTHON_PROJECTS\\new_studing\\output\\password_list.txt', 'w', encoding='utf-8') as f:
            for i in password_list:
                f.write(i+'\n')

    else:
        for i in password_list:
            print(i)

# ready


def get_replce_symbols(change_symbols):
    change_symbols_from, change_symbols_to = '', ''

    if change_symbols:
        change_symbols_from, change_symbols_to = change_symbols

    return change_symbols_from, change_symbols_to

# ready


def replace_symbols(change_symbols_from, change_symbols_to, password_list):
    new_password_list = []
    for i in password_list:
        modified_word = i.replace(change_symbols_from, change_symbols_to)
        new_password_list.append(modified_word)

    return new_password_list

# ready


if __name__ == "__main__":
    print('Before that you start program enter command: python passwords_generator.py --help')
    start_program()