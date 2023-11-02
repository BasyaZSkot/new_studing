from random import choice

import click

import os

file_name = 'password_list.txt'
folder_name = 'output'
FILE_OUTPUT_PATH = os.path.abspath(f"{folder_name}/{file_name}")


@click.command()
@click.option('--password_num', '-pn', type=int, default=1, help='Count of password.', show_default=True)
@click.option('--word_num', '-wn', type=int, default=1, help='How many words in password.', show_default=True)
@click.option('--dictionary_of_words', '-df', type=str, default='dictionaries/basic_list_of_words.txt', help="Path of dictionary. Example: folder_name/file_name. If you want to use your dictionary, you need to add this file in 'dictionaries'.", show_default=True)
@click.option('--separators', '-s', type=str, default='', help='Spaces in your password.', show_default=True)
@click.option('--change_symbols', '-ch', default=('', ''), type=str, multiple=True, help="Symbols which will change.", show_default=True)
@click.option('--passwords_in_file', '-pif', default=True, help='This variable indicates whether passwords will be written to the file', show_default=True, is_flag=True)

def start_program(password_num, word_num, dictionary_of_words, separators, change_symbols, passwords_in_file):

    dictionary_of_words = get_dictionary(dictionary_of_words)
    change_symbols_from, change_symbols_to = get_replce_symbols(change_symbols)

    password_list = basic_passwords_list(
        password_num, word_num, dictionary_of_words)
    password_list = passwords_with_separatores(separators, password_list)
    password_list = replace_symbols(
        change_symbols_from, change_symbols_to, password_list)
    write_passwords_in_file(password_list, passwords_in_file)


def basic_passwords_list(password_num, word_num, dictionary_of_words):
    passwords_list = []

    for i in range(password_num):
        words_list = []

        for _ in range(word_num):
            words_list.append(choice(dictionary_of_words))

        passwords_list.append(words_list)

    return passwords_list


def get_dictionary(dictionary_of_words):
    dictionary_of_words = dictionary_of_words.split('/')
    folder_name, file_name = dictionary_of_words
    FILE_PATH = os.path.abspath(f"{folder_name}/{file_name}")

    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        new_dictionary = f.read()
        new_dictionary = new_dictionary.split()

    return new_dictionary


def passwords_with_separatores(separators, password_list):

    new_password_list = []

    for i in password_list:
        modified_word = separators.join(list(i))
        new_password_list.append(modified_word)

    return new_password_list


def write_passwords_in_file(password_list, passwords_in_file):
    if passwords_in_file:
        with open(FILE_OUTPUT_PATH, 'w', encoding='utf-8') as f:
            for i in password_list:
                f.write(i + '\n')

    else:
        for i in password_list:
            print(i)


def get_replce_symbols(change_symbols):
    change_symbols_from, change_symbols_to = change_symbols

    return change_symbols_from, change_symbols_to


def replace_symbols(change_symbols_from, change_symbols_to, password_list):
    new_password_list = []
    for i in password_list:
        modified_word = i.replace(change_symbols_from, change_symbols_to)
        new_password_list.append(modified_word)

    return new_password_list


if __name__ == "__main__":
    print('Before that you start program enter command: python passwords_generator.py --help')
    start_program()