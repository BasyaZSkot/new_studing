from password_generator import add_separator as func


def test_add_separator_():
    separator = '_'
    list_of_passwords = [['fishing', 'dog', 'cat', 'purple', 'school'], [
        'football', 'ball', 'table', 'chair', 'dish']]

    assert func(separator, list_of_passwords) == [
        'fishing_dog_cat_purple_school', 'football_ball_table_chair_dish']


def test_add_separator_noth():
    separator = ''
    list_of_passwords = [['fishing', 'dog', 'cat', 'purple', 'school'], [
        'football', 'ball', 'table', 'chair', 'dish']]

    assert func(separator, list_of_passwords) == [
        'fishingdogcatpurpleschool', 'footballballtablechairdish']
