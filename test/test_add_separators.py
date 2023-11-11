from src.password_generator import add_separator


def test_add_separator_underscore():
    # given
    separator = '_'
    list_of_passwords = [['fishing', 'dog', 'cat', 'purple', 'school'], [
        'football', 'ball', 'table', 'chair', 'dish']]
    
    # when
    passwords_list_with_separators = add_separator(separator, list_of_passwords)

    # then
    assert passwords_list_with_separators == [
        'fishing_dog_cat_purple_school', 'football_ball_table_chair_dish']


def test_add_separator_noth():
    # given
    separator = ''
    list_of_passwords = [['fishing', 'dog', 'cat', 'purple', 'school'], [
        'football', 'ball', 'table', 'chair', 'dish']]
    
    # when
    passwords_list_with_separators = add_separator(separator, list_of_passwords)

    # then
    assert passwords_list_with_separators == [
        'fishingdogcatpurpleschool', 'footballballtablechairdish']
