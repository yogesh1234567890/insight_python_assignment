'''1. Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
'''
import collections
string = 'google.com'
frequencies = collections.Counter(string)
repeated = {}

for key, value in frequencies.items():
    if value >=0:
        repeated[key] = value

print(repeated)
