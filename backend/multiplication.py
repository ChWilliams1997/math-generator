from equation import Equation

class Multiplication(Equation):
  """ This class holds the code to generate mutliplication problems
  """
  def beginner(self) -> str:
    """ Generates a beginner level multiplication problem

        Returns
        -------
        str -
          The beginner level multiplication expression
    """
    nums = self.generateIntegers(2, [(0, 10)])
    x, y = nums[0], nums[1]
    return f'{x} * {y}'

  def standard(self) -> str:
    """ Generates a standard level multiplication problem

        Returns
        -------
        str -
          The standard level multiplication expression
    """
    nums = self.generateIntegers(2, [(0, 150)])
    x, y = nums[0], nums[1]
    return f'{x} * {y}'

  def advanced(self) -> str:
    """ Generates an advanced level multiplication problem

        Returns
        -------
        str -
          The advanced level multiplication expression
    """
    nums = self.generateIntegers(2, [(0, 500)])
    x, y = nums[0], nums[1]
    return f'{x} * {y}'