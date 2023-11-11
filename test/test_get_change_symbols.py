from src.password_generator import get_replce_symbols


def test_change_symbols_a_b():
    # given
    change_symbols = ('a', 'b')

    # when
    first_symb, second_symb = get_replce_symbols(change_symbols)

    # then
    assert first_symb == 'a'
    assert second_symb == 'b'


def test_change_symbols_noth_noth():
    # given
    change_symbols = ('', '')

    # when 
    first_symb, second_symb = get_replce_symbols(change_symbols)

    # then 
    assert first_symb == ''
    assert second_symb == ''
