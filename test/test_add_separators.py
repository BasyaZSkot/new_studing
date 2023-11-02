import sys

sys.path.append('C:\\Users\\User\\PYTHON_PROJECTS\\studing\\code')

from passwords_generator import separators_and_new_password_list as func

tests_parametr1 = '_'
tests_parametr2 = [['fishing', 'fishing', 'fishing'], ['fishing', 'fishing', 'fishing']]
tests_parametr3 = ''

def test_1():
    assert type(func(tests_parametr1, tests_parametr2)) == list
    assert func(tests_parametr1, tests_parametr2) == ['fishing_fishing_fishing', 'fishing_fishing_fishing']

def test_2():
    assert type(func(tests_parametr3, tests_parametr2)) == list
    assert func(tests_parametr3, tests_parametr2) == ['fishingfishingfishing', 'fishingfishingfishing']