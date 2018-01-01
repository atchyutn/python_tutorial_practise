'''
This program is to practise the use case of init function in a python class
'''

class Game():
  """
  [summary]: This class initialises the energy variable and prints out its value for every player object.
  """
  def __init__(self, x):
    self.energy = x

  def energy_level(self):
    """[summary]: This method returns the enery level of a player.
    """
    print(self.energy)


player1 = Game(10)
player2 = Game(50)

player1.energy_level()
player2.energy_level()