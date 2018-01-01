'''
This program is to practise the concpets of inheritance and overriding in python
'''
class Parent():
  """
  [summary]: This class prints the parent name for the child class
  """
  def parent_name(self):
    print("Nagabhairava")


class Child(Parent):
  """
  [summary]: This class prints the child name & the parent name which is overrided.
  """
  def child_name(self):
    print("Atchyut")

  def parent_name(self):
    print("Kesineni")
  
Atchyut = Child()
Atchyut.child_name()
Atchyut.parent_name()