'''
This program scrape the top tv shows listed in the IMDB website.
Disclaimer: This program is completely educational purpose and not used or will be used anywhere
'''

import requests
from bs4 import BeautifulSoup

url = 'http://www.imdb.com/chart/toptv/?ref_=nv_tvv_250_3'

def imdb_tv_scraper(url):
  source_code = requests.get(url).text
  soup = BeautifulSoup(source_code, "lxml")
  show_names = soup.find_all('td', {'class': 'titleColumn'})
  for show in show_names:
    show = show.find_all('a')
    print(show[0].string)

imdb_tv_scraper(url)
