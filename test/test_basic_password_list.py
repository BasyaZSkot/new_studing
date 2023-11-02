import sys

sys.path.append('C:\\Users\\User\\PYTHON_PROJECTS\\studing\\code')

from passwords_generator import basic_passwords_list as func

tests_parametr1 = 2
tests_parametr2 = 3
tests_parametr3 = ['fishing']

def test_1():
    assert func(tests_parametr1, tests_parametr2, tests_parametr3) == [['fishing', 'fishing', 'fishing'], ['fishing', 'fishing', 'fishing']]