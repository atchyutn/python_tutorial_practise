'''
This program is to find the largest and smallest of the values
'''

import heapq

stocks = [
  {'ticker': 'sbi', 'price': 239},
  {'ticker': 'ab', 'price': 129},
  {'ticker': 'jio', 'price': 1100}
]

small_2 = heapq.nsmallest(2, stocks, key = lambda stock: stock['price'])

print(small_2)