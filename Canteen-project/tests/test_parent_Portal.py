import pytest
from canteen_project.parent_portal import ParentPortal,Operations


def test_Set_Max_Daily():
    
    actual = Operations.max_daily_credit(1,3.5)
    expected = {'id': 1, 'name': 'Ali', 'Balance': 0.0, 'Max Daily Credit': 3.5, 'Not Allowed Items': None, 'Daily meal': None}
    assert actual == expected

def test_get_std_data():
    P1= ParentPortal()
    AllstdInfo = P1._get_students_data()
    actual = AllstdInfo[0]
    expected = {'id': 2022458, 'name': 'Ahmad', 'Balance': 0.0, 'Max Daily Credit': 1.0, 'Not Allowed Items': None, 'Daily meal': None}
    assert actual == expected


