"""
Find the sum of numbers
"""

def sum_of_numbers(*args):
  """[summary]:Function to find the sum of given numbers
  Arguments:
    *args {[type]} -- [any number of integers]
  """
  sum_total = 0
  for num in args:
    sum_total += num
  print(sum_total)

sum_of_numbers(10, 20, 20)
