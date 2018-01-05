'''
Program to practise structs in python
'''

from struct import *

#store as bytes data
packed_data = pack('iif',1,6,7.3)
print(packed_data)

#converting byte data into normal values
unpacked_data = unpack('iif',packed_data)
print(unpacked_data)