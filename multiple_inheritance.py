'''
This program is to practise the muliple inheritance in python
'''

class Mario():
  """[summary]
  In this class, Mario has a power to move and fire
  [description]
  """
  
  def move(self):
    print("Hey, I'm moving")

  def fire(self):
    print("Hey, I can fire now")


class Mashroom():
  """[summary]
  In this class, Mario has power to eat mashroom
  [description]
  """
    
  def eat(self):
    print("Hey, I ate mashroom and grown big")


class BigMario(Mario, Mashroom):
  """[summary]
  In this class, Mario has all the powers inherited from above two classes
  [description]
  """
  
  pass


mario = BigMario()
mario.eat()
mario.fire()
mario.move()