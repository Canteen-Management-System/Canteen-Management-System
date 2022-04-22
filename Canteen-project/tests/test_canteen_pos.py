from canteen_project.canteen_pos import CanteenSystem


def test_greeting():
    greeting = CanteenSystem.greeting()
    actual = greeting
    expected = '''===================================
   Welcome to the Canteen System
===================================
              '''
    assert actual == expected
