'''
This program is used to count the occurances of a word in a given set of words
'''
user_input = input('Please enter a comma seperated list of words:')

def word_frequency(user_input):
  word_count = {}
  word_array = user_input.split(',')
  for word in word_array:
    if word in word_count:
      word_count[word] += 1
    else:
      word_count[word] = 1
  for key, value in word_count.items():
    print(key,value)


word_frequency(user_input)