from tests.flow.flo import Flo


def test_pay_cash():
    Flo.test("tests/flow/cash.sim.txt")
