'''
This program is to practise threding concepts in python
'''

import threading


class BukyMessanger(threading.Thread):
  def run(self):
    for _ in range(10):
      print(threading.currentThread().getName())



x = BukyMessanger(name = "Message Sent")
y = BukyMessanger(name = "Recieve Message")

x.start()
y.start()