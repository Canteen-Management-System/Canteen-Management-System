from canteen_project.helper_methods import HelperMethods
from tests.flow.flo import Flo
from canteen_project.helper_methods import HelperMethods as hm
import pytest


def test_pay_cash():
    Flo.test("tests/flow/cash_with_one_order.sim.txt")


def test_run_and_quit():
    Flo.test("tests/flow/run_and_quit.sim.txt")


def test_cash_with_multi_orders():
    Flo.test("tests/flow/cash_with_multi_orders.sim.txt")


def test_max_daily_credit():
    Flo.test("tests/flow/max_daily_credit.sim.txt")


@pytest.fixture(autouse=True)
def clean():
    """runs before each test automatically.
    This is necessary because otherwise any function will effect the other test result 
    """
    _hm = hm()
    students_data = hm.get_data('Student_info.json')
    for student in students_data:
        if student['id'] == 2022458:
            student["Balance"] = 500
            _hm.set_student_info(students_data, student, 0)
            break
