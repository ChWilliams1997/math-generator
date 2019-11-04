from equation import Equation

class Addition(Equation):
  """ This class holds the code to generate addition problems
  """
  def beginner(self) -> str:
    """ Generates a beginner level addition problem

        Returns
        -------
        str -
          The beginner level addition expression
    """
    nums = self.generateIntegers(2, [(1, 20)])
    x, y = nums[0], nums[1]
    return f'{x} + {y}'

  def standard(self) -> str:
    """ Generates a standard level addition problem

        Returns
        -------
        str -
          The standard level addition expression
    """
    nums = self.generateIntegers(2, [(10, 500)])
    x, y = nums[0], nums[1]
    return f'{x} + {y}'

  def advanced(self) -> str:
    """ Generates an advanced level addition problem

        Returns
        -------
        str -
          The advanced level addition expression
    """
    nums = self.generateIntegers(3, [(50, 2000)])
    x, y, z = nums[0], nums[1], nums[2]
    if self.generateDecimals(1, 100)[0] <= 70:
      return f'{x} + {y} + {z}'
    else:
      return f'{x} + {y}'
