import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 3, 3) == 9

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 2, 2) == 1

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 2, 2) == 0

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 3, 5) == 6

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_adding_unsuccess(self):
        assert self.calc.adding(self, 1, 1) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')