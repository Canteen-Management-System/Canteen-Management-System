from tests.flow.flo import Flo


def test_pay_cash():
    Flo.test("tests/flow/cash_with_one_order.sim.txt")


def test_run_and_quit():
    Flo.test("tests/flow/run_and_quit.sim.txt")


def test_cash_with_multi_orders():
    Flo.test("tests/flow/cash_with_multi_orders.sim.txt")


def test_cash_with_multi_orders():
    Flo.test("tests/flow/max_daily_credit.sim.txt")
