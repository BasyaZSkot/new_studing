import sys

sys.path.append('C:\\Users\\User\\PYTHON_PROJECTS\\studing\\code')

from passwords_generator import replace_symbols as func

tests_parametr1 = 'a'
tests_parametr2 = 'b'
tests_parametr3 = ''
tests_parametr4 = ''
tests_parametr5 = ['cat_cat_cat', 'cat_cat_cat']
tests_parametr6 = ['fishing_fishing_fishing', 'fishing_fishing_fishing']


def test_1():
    assert type(func(tests_parametr1, tests_parametr2, tests_parametr5)) == list
    assert func(tests_parametr1, tests_parametr2, tests_parametr5) == ['cbt_cbt_cbt', 'cbt_cbt_cbt']

def test_2():
    assert type(func(tests_parametr3, tests_parametr4, tests_parametr6)) == list
    assert func(tests_parametr3, tests_parametr4, tests_parametr6) == ['fishing_fishing_fishing', 'fishing_fishing_fishing']