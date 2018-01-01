'''
program to download a infosys stock data from internet

Disclaimer: This code is just for learning purpose, It was not used or will not be used any where.
from urllib import request
'''
infy_url = "https://query1.finance.yahoo.com/v7/finance/download/INFY?period1=1512118192&period2=1514796592&interval=1d&events=history&crumb=dVBJ/YkeyWz"
def download_csv(csv_url):
  """[summary]: Method to read a CSV from internet and write it into a local csv file
  Arguments:
    csv_url {[type]} -- [An url from which file is downloaded]
  """
  response = request.urlopen(csv_url)
  csv = response.read()
  csv_str = str(csv)
  lines = csv_str.split("\\n")
  dest_url = r"sample.csv"
  fx = open(dest_url, 'w')
  for line in lines:
    fx.write(line + "\n")
  fx.close()


download_csv(infy_url)