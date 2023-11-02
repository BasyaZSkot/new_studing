import sys

sys.path.append('C:\\Users\\User\\PYTHON_PROJECTS\\studing\\code')
sys.path.append('C:\\Users\\User\\PYTHON_PROJECTS\\studing\\dictionaries')

from list_of_words import programs_dictionary
from passwords_generator import get_dictionary_2_0 as func

tests_parametr1 = ('fishing', 'growth', 'income', 'marriage',
                   'user', 'combination', 'failure')

tests_parametr2 = False


def test_1():
    assert type(func(tests_parametr1)) == list
    assert func(
        tests_parametr1) == ['fishing', 'growth', 'income', 'marriage', 'user', 'combination', 'failure']

def test_2():
    assert type(func(tests_parametr2)) == list
    assert func(tests_parametr2) == programs_dictionary