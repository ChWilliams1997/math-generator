from equation import Equation

class Subtraction(Equation):
  """ This class holds the code to generate subtraction problems
  """
  def beginner(self) -> str:
    """ Generates a beginner level subtraction problem

        Returns
        -------
        str -
          The beginner level subtraction expression
    """
    nums = self.generateIntegers(2, [(1, 20)])
    x, y = nums[0], nums[1]
    return f'{x} - {y}'

  def standard(self) -> str:
    """ Generates a standard level subtraction problem

        Returns
        -------
        str -
          The standard level subtraction expression
    """
    nums = self.generateIntegers(2, [(10, 500)])
    x, y = nums[0], nums[1]
    if x > y:
      (x, y) = (y, x)
    return f'{x} - {y}'

  def advanced(self) -> str:
    """ Generates an advanced level subtraction problem

        Returns
        -------
        str -
          The advanced level subtraction expression
    """
    nums = self.generateIntegers(3, [(50, 2000)])
    x, y, z = nums[0], nums[1], nums[2]
    if self.generateDecimals(1, 100)[0] <= 70:
      return f'{x} - {y} - {z}'
    else:
      return f'{x} - {y}'