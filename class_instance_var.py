'''
This program is to practise the class and instance variables
'''

class Girl:
  """
  [summary]:This class assigns a name for a girl object with same gender
  """
  gender = "female"
  def __init__(self, name):
    self.name = name

Richa = Girl("richa")
Anushka = Girl("Anuska")

print(Richa.gender)
print(Anushka.gender)
print(Richa.name)
print(Anushka.name)
    