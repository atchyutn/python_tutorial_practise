'''
This program unpacks the list and find the avarage of the value present in middle
and drop the first and last values in the array
'''
def find_middle_values_avg(grades):
  first, *middle, last = grades
  avg = sum(middle)/len(middle)
  print(avg)


find_middle_values_avg([100, 20, 30, 40, 200])