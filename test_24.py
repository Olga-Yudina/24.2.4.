import pytest
from app.calc import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 5, 5) == 25

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 10, 5) == 5

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 5, 5) == 10
