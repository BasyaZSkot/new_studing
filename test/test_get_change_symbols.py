from password_generator import add_separator as func

def test_change_symbols_a_b():
    change_symbols = ('a', 'b')

    first_symb, second_symb = func(change_symbols)
    assert first_symb == 'a'
    assert second_symb == 'b'


def test_change_symbols_noth_noth():
    change_symbols = ('', '')

    first_symb, second_symb = func(change_symbols)
    assert first_symb == ''
    assert second_symb == ''
