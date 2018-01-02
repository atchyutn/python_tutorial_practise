'''
In this program we are going to zip two lists
'''

list1 = ["Hena", "Steve", "Bill"]
list2 = ["Baker", "Jobs", "Gates"]

def zip_lists(list1, list2):
  zipped_list = zip(list1,list2)
  print(zipped_list)

zip_lists(list1, list2)