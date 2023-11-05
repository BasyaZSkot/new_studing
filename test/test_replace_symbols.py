from src.password_generator import replace_symbols


def test_replace_a_with_b():
    # given
    change_symbols_from = 'a'
    change_symbols_to = 'b'
    list_of_passwords = ['cat_dog_school_atack', 'dog_phone_case_table']

    # when 
    password_list_with_replace_symboles = replace_symbols(change_symbols_from, change_symbols_to, list_of_passwords)

    # then
    assert password_list_with_replace_symboles == [
        'cbt_dog_school_btbck', 'dog_phone_cbse_tbble']


def test_replace_noth_with_noth():
    # given
    change_symbols_from = ''
    change_symbols_to = ''
    list_of_passwords = ['cat_dog_school_atack', 'dog_phone_case_table']

    # when 
    password_list_with_replace_symboles = replace_symbols(change_symbols_from, change_symbols_to, list_of_passwords)

    # then
    assert password_list_with_replace_symboles == [
        'cat_dog_school_atack', 'dog_phone_case_table']
