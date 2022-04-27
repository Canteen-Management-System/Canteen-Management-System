from canteen_project.canteen_pos import CanteenSystem as CS
from canteen_project.helper_methods import HelperMethods as hm
import pytest


"""
    ! The cash should not be in minus
    What to test:
        [1] _get_menu 
        [2] _store_items
        [3] check_not_allowed_items
        [4] _select_from_category
        [5] recipe
        [6] _id_search
        [7] _is_cart_empty

    how to remove the color from test
    Mohammed problem
    how to switch to windows and if it works on mac
    should we test the methods thad need input

"""

cs = CS()


def test_get_menu_method():
    actual = cs._get_menu('Hot food')
    expected = ['Peppers with pizazz',
                'Hot peppers are among the most well-known spicy foods and their heat is thanks to a compound called capsaicin', 2.0]
    assert actual[0] == expected


def test_not_allowed_item_for_student_2022458(get_students):
    student = get_students[0]
    actual_id = student['id']
    expected_id = 2022458
    assert actual_id == expected_id

    not_alloed_items = student['Not Allowed Items']
    selected_item = "Peppers with pizazz"
    actual = True if selected_item in not_alloed_items else False
    expected = True
    assert actual == expected


@pytest.fixture
def get_students():
    return hm.get_data('Student_info.json')
