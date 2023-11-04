from code.password_generator import add_separator as func


def test_our_dictionary():
    dictionary_path = 'dictionaries/new_list_of_words.txt'
    assert func(dictionary_path) == ['VASYA', 'ZELDIN', 'IOSIFOVICH']
