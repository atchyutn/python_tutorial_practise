'''
This program is to practise the basic concepts of classes and objects in python
'''
class Game:
  """
  [summary]: Game class to attack or to find the life left
  """
  life = 3

  def attack(self):
    """
    [summary]: This method will attack the gamer and reduce his life
    """
    print("ouch!")
    self.life -= 1
  def life_count(self):
    """[summary]: This method returns the left life count of the gamer
    """
    print(str(self.life) + "Lives left")

gamer1 = Game()
gamer1.attack()
gamer1.attack()
gamer1.life_count()

gamer2 = Game()
gamer2.attack()
gamer2.life_count()
