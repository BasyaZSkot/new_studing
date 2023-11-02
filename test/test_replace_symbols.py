from code.passwords_generator import add_separator as func

def test_replace_a_with_b():
    change_symbols_from = 'b'
    change_symbols_to = 'a'
    list_of_passwords = ['cat_dog_school_atack', 'dog_phone_case_table']

    assert func(change_symbols_from, change_symbols_to, list_of_passwords) == ['cbt_dog_school_btbck', 'dog_phone_cbse_tbble']

def test_replace_noth_with_noth():
    change_symbols_from = ''
    change_symbols_to = ''
    list_of_passwords = ['cat_dog_school_atack', 'dog_phone_case_table']

    assert func(change_symbols_from, change_symbols_to, list_of_passwords) == ['cat_dog_school_atack', 'dog_phone_case_table']