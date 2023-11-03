from password_generator import add_separator as func

def test_basic_password_list():
    passwords_num = 2
    words_num = 3
    dictionary_of_words = ['fishing', 'dog', 'cat', 'purple', 'school']

    basic_passwords_list = func(passwords_num, words_num, dictionary_of_words)
    for passwords in basic_passwords_list:
        for words in passwords:
            assert words in dictionary_of_words == True