'''
Practise map function in python
'''

incomes = [10,20,20]

def double_dollars(income):
  return income * 2

mapped_list = list(map(double_dollars,incomes))
print(mapped_list)
