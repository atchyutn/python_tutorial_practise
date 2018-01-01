#program to download image from internet

import random
import urllib.request

def download_image_from_web(url):
  """[This function downloads image from internet]
  [We download image from internet using urllib]
  Arguments:
    url {[string]} -- [Its a url string of any image on the internet]
  """
  num = random.randrange(1, 1000)
  full_name = str(num)+".jpg"
  urllib.request.urlretrieve(url, full_name)

download_image_from_web("http://www.berandom.ca/wp-content/uploads/2017/03/Logo-3-inches.png")
