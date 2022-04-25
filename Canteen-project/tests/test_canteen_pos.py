from canteen_project.canteen_pos import CanteenSystem

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

"""


def test_greeting():
    greeting = CanteenSystem.greeting()
    actual = greeting
    expected = '''===================================
   Welcome to the Canteen System
===================================
              '''
    assert actual == expected
