from src.password_generator import basic_passwords_list 


def test_basic_password_list():
    # given
    passwords_num = 2
    words_num = 3
    dictionary = ['fishing', 'dog', 'cat', 'purple', 'school']

    # when
    passwords_list = basic_passwords_list(passwords_num, words_num, dictionary)
    
    # then
    for passwords in passwords_list:
        for words in passwords:
            assert words in dictionary

def test_lenth_of_password_list():
    # given
    passwords_num = 2
    words_num = 3
    dictionary = ['fishing', 'dog', 'cat', 'purple', 'school']

    # when
    passwords_list = basic_passwords_list(passwords_num, words_num, dictionary)
    
    # then
    assert len(passwords_list) == 2
    assert len(passwords_list[0]) == 3
    assert len(passwords_list[1]) == 3
