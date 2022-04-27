import pytest
from canteen_project.parent_portal import ParentPortal, Operations
import json


# test for Set the Max daily credit
def test_Set_Max_Daily():

    actual = Operations.max_daily_credit(1, 3.5)
    expected = {'id': 1, 'name': 'Ali', 'Balance': 0.0,
                'Max Daily Credit': 3.5, 'Not Allowed Items': [], 'Daily meal': []}
    assert actual == expected


# Test for get the student data and test the first row
def test_get_std_data():
    P1 = ParentPortal()
    AllstdInfo = P1._get_students_data()
    actual = AllstdInfo[0]
    expected = {'id': 2022458, 'name': 'Ahmad', 'Balance': 499.65,
                'Max Daily Credit': 2.0, 'Not Allowed Items': ['Peppers with pizazz'], 'Daily meal': []}
    assert actual == expected


# Test for the Recharge method
def test_Recharge_Blalnce():
    actual = Operations.recharge(1, 200)
    expected = {'id': 1, 'name': 'Ali', 'Balance': 200,
                'Max Daily Credit': 0, 'Not Allowed Items': [], 'Daily meal': []}
    assert actual == expected

#


@pytest.fixture(autouse=True)
def clean():
    """runs before each test automatically.
    This is necessary because otherwise any function will effect the other test result 
    """
    P1 = ParentPortal()
    AllstdInfo = P1._get_students_data()
    for p in AllstdInfo:
        if p['id'] == 2022458:
            continue
        p["Balance"] = 0
        p["Max Daily Credit"] = 0
        p["Not Allowed Items"] = []
        p["Daily meal"] = []
        # Serializing json
    json_object = json.dumps(AllstdInfo, indent=4)
    # Writing to sample.json
    with open('Student_info.json', "w") as outfile:
        outfile.write(json_object)
