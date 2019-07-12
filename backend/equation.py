from random import randint, random


class Equation():
  """The base class for equations that can be solved
     with the eval function
  """
  def generateIntegers(self, nums_to_generate : int, ranges : list) -> list:
    """ Generates random integers based on the given amount
        and ranges

        Parameters
        ----------
        nums_to_generate : int -
          The amount of integers to generate
   
        ranges : list -
          A list of tuples that contain the upper and lower
          limits for number generation
   
        Returns
        -------
        list -
          A list of randomly generated numbers 
    """
    nums = list()
    for i in range(nums_to_generate):
      try:
        nums.append(randint(ranges[i][0], ranges[i][1]))
      except:
        nums.append(randint(ranges[0][0], ranges[0][1]))
    return nums

  def generateDecimals(self, nums_to_generate : int, multiplier : int) -> list:
    """ Generates random floats based on the given amount
        and multiplies each result by the given multiplier

        Parameters
        ----------
        nums_to_generate : int -
          the amount of floats to generate

        multiplier : int -
          the number to multiply the generated result by
        
        Returns
        -------
        list -
          a list of floats generated
    """
    nums = list()
    for i in range(nums_to_generate):
      nums.append(random() * multiplier)
    return nums

  def solve(self, equation : str):
    """ Solves the given equation using the eval function

        Parameters
        ----------
        equation : str -
          a mathematical equation that contains zero variables
    """
    return eval(equation)