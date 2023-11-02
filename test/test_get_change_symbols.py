import sys

sys.path.append('C:\\Users\\User\\PYTHON_PROJECTS\\studing\\code')

from passwords_generator import get_replce_symbols as func

tests_parametr1 = ('a', 'b')
tests_parametr2 = False

def test_1():
    first_answ, second_answ = func(tests_parametr1)
    assert first_answ == 'a', 'b'

def test_2():
    first_answ, second_answ = func(tests_parametr2)
    assert first_answ == '', ''
