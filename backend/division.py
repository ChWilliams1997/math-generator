from equation import Equation


class Division(Equation):
  """ This class holds the code for division problems
  """

  def beginner(self) -> str:
    """ Generates a beginner level division problem

        Returns
        -------
        str -
          The beginner level division expression
    """
    x, y = 2, 3
    try:
      while x % y != 0 and y % x != 0:
        nums = self.generateIntegers(2, [(0, 100)])
        x, y = nums[0], nums[1]
    except ZeroDivisionError:
      pass

    return f'{x} / {y}' if x >= y and y > 0 else f'{y} / {x}'

  def standard(self) -> str:
    """ Generates a standard level division problem

        Returns
        -------
        str -
          The standard level division expression
    """
    x, y = 2, 3
    try:
      while x % y != 0 and y % x != 0:
        nums = self.generateIntegers(2, [(0, 22500)])
        x, y = nums[0], nums[1]
    except ZeroDivisionError:
      pass

    return f'{x} / {y}' if x >= y and y > 0 else f'{y} / {x}'

  def advanced(self) -> str:
    """ Generates an advanced level division problem

        Returns
        -------
        str -
          The advanced level division expression
    """
    x, y = 2, 3
    try:
      while x % y != 0 and y % x != 0:
        nums = self.generateIntegers(2, [(0, 250000)])
        x, y = nums[0], nums[1]
    except ZeroDivisionError:
      pass

    return f'{x} / {y}' if x >= y and y > 0 else f'{y} / {x}'
