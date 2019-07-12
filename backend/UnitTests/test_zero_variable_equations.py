import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from addition import Addition

def test_addition_solve():
  add = Addition()
  assert add.solve('2 + 2') == 4
  assert add.solve('2 + -2') == 0