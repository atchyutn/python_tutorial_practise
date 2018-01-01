'''
Program to write a text file using python
'''
file_write = open('sample.txt', 'w')
file_write.write("This is the line I want to write in the text file\n")
file_write.write("Here is the second line I want to add\n")
file_write.close()


'''
Program to read the file created above
'''
file_read = open('sample.txt', 'r')
text = file_read.read()
print(text)
file_read.close()