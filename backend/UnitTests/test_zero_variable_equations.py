import os, sys
import unittest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from addition import Addition
from subtraction import Subtraction
from multiplication import Multiplication
from division import Division

class TestZeroVariableEquations(unittest.TestCase):
  def setUp(self):
    self.addition = Addition()
    self.subtraction = Subtraction()
    self.multiplication = Multiplication()
    self.division = Division()

  def test_addition_ranges_beginner(self):
    for i in range(10):
      x, y = self.addition.beginner().split('+')
      assert (int(x) >= 0) and (int(x) <= 20)
      assert (int(y) >= 0) and (int(y) <= 20)

  def test_addition_ranges_standard(self):
    for i in range(10):
      x, y = self.addition.standard().split('+')
      assert (int(x) >= 10) and (int(x) <= 500)
      assert (int(y) >= 10) and (int(y) <= 500)

  def test_addition_ranges_advanced(self):
    for i in range(10):
      z = 0
      expression = self.addition.advanced()
      try:
        x, y, z = expression.split('+')
      except ValueError:
        x, y = expression.split('+')
      
      assert (int(x) >= 50) and (int(x) <= 2000)
      assert (int(y) >= 50) and (int(y) <= 2000)
      if z != 0:
        assert (int(z) >= 50) and (int(z) <= 2000)

  def test_addition_solve(self):
    assert self.addition.solve('2 + 2') == 4
    assert self.addition.solve('2 + -2') == 0
    assert self.addition.solve('-2 + 2') == 0

  def test_subtraction_ranges_beginner(self):
    for i in range(10):
      x, y = self.subtraction.beginner().split('-')
      assert (int(x) >= 0) and (int(x) <= 20)
      assert (int(y) >= 0) and (int(y) <= 20)

  def test_subtraction_ranges_standard(self):
    for i in range(10):
      x, y = self.subtraction.standard().split('-')
      assert (int(x) >= 10) and (int(x) <= 500)
      assert (int(y) >= 10) and (int(y) <= 500)

  def test_subtraction_ranges_advanced(self):
    for i in range(10):
      z = 0
      expression = self.subtraction.advanced()
      try:
        x, y, z = expression.split('-')
      except ValueError:
        x, y = expression.split('-')
        
      assert (int(x) >= 50) and (int(x) <= 2000)
      assert (int(y) >= 50) and (int(y) <= 2000)
      if z != 0:
        assert (int(z) >= 50) and (int(z) <= 2000)

  def test_subtraction_solve(self):
    assert self.subtraction.solve('2 - 2') == 0
    assert self.subtraction.solve('2 - -2') == 4
    assert self.subtraction.solve('-2 - 2') == -4
    assert self.subtraction.solve('-2 - -2') == 0

  def test_multiplication_ranges_beginner(self):
    for i in range(10):
      x, y = self.multiplication.beginner().split('*')
      assert (int(x) >= 0) and (int(x) <= 10)
      assert (int(y) >= 0) and (int(y) <= 10)

  def test_multiplication_ranges_standard(self):
    for i in range(10):
      x, y = self.multiplication.standard().split('*')
      assert (int(x) >= 0) and (int(x) <= 150)
      assert (int(y) >= 0) and (int(y) <= 150)

  def test_multiplication_ranges_advanced(self):
    for i in range(10):
      x, y = self.multiplication.advanced().split('*')
      assert (int(x) >= 0) and (int(x) <= 500)
      assert (int(y) >= 0) and (int(y) <= 500)

  def test_multiplication_solve(self):
    assert self.multiplication.solve('2 * 2') == 4
    assert self.multiplication.solve('-2 * 2') == -4
    assert self.multiplication.solve('2 * 0') == 0
    assert self.multiplication.solve('0 * 2') == 0

  def test_division_ranges_beginner(self):
    for i in range(10):
      x, y = self.division.beginner().split('/')
      assert (int(x) >= 0) and (int(x) <= 100)
      assert (int(y) >= 0) and (int(y) <= 100)

  def test_division_ranges_standard(self):
    for i in range(10):
      x, y = self.division.standard().split('/')
      assert (int(x) >= 0) and (int(x) <= 22500)
      assert (int(y) >= 0) and (int(y) <= 22500)

  def test_division_ranges_advanced(self):
    for i in range(10):
      x, y = self.division.standard().split('/')
      assert (int(x) >= 0) and (int(x) <= 250000)
      assert (int(y) >= 0) and (int(y) <= 250000)

  def test_division_solve(self):
    assert self.division.solve('2/2') == 1
    assert self.division.solve('-2/2') == -1
    assert self.division.solve('2/-2') == -1

  def test_division_numbers_result_in_remainder_zero_beginner(self):
    for i in range(10):
      x, y = self.division.beginner().split('/')
      assert (x % y == 0) or (y % x == 0)

  def test_division_numbers_result_in_remainder_zero_standard(self):
    for i in range(10):
      x, y = self.division.standard().split('/')
      assert (x % y == 0) or (y % x == 0)

  def test_division_numbers_result_in_remainder_zero_advanced(self):
    for i in range(10):
      x, y = self.division.advanced().split('/')
      assert (x % y == 0) or (y % x == 0)