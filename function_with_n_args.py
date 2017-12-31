def sum_of_numbers(*args):
  sum = 0
  for n in args:
    sum += n
  print(sum)

sum_of_numbers(10,20,20)