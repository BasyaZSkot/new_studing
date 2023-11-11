from src.password_generator import get_dictionary


def test_our_dictionary():
    # given
    dictionary_path = 'dictionaries/tests_list_of_words.txt'
    
    # when
    dictionary = get_dictionary(dictionary_path)

    # then
    assert  dictionary == ['VASYA', 'ZELDIN', 'IOSIFOVICH']
