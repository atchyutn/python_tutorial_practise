'''
This program is to find the min, max, sorted list of stocks based on the value
'''

#creating dictonary with key, value pairs of company and its share value
STOCKS = {
  'SBI' : 239,
  'Infosys': 1190,
  'Airtel': 390,
  'wipro' : 500
}

'''
To find the min or max or sorted values of a dict, we need to zip.
'''

min_stock = min(zip(STOCKS.values(), STOCKS.keys()))
print(min_stock)

max_stock = max(zip(STOCKS.values(), STOCKS.keys()))
print(max_stock)

sorted_stocks = sorted(zip(STOCKS.values(), STOCKS.keys()))
print(sorted_stocks)