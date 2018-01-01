'''
This program is to practise exceptions in python
'''

while True:
  try:
    number = int(input("What's your fav number hoss?\n"))
    print(number)
    break
  except ValueError:
    print("Please enter only number")
  except ZeroDivisionError:
    print("Please don't pick zero")
  except:
    break
  finally:
    print("loop executed!")