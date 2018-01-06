'''
This program is to sort custom objects using attrGetter from operator
'''

from operator import attrgetter

class User:
  
  def __init__(self, x, y):
    self.name = x
    self.user_id = y

  def __repr__(self):
    return self.name + " : " + str(self.user_id)


users = [
  User('Atchyut', 35),
  User('Nikhil', 55),
  User('Shivani', 9),
  User('Harish', 47),
  User('Teja', 5)
]

for user in users:
  print(user)

print('------------------')
for user in sorted(users, key=attrgetter('name')):
  print(user)

print('-------------------')
for user in sorted(users, key=attrgetter('user_id')):
  print(user)
