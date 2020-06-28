'''2.​ Write a Python program to get a string made of the first 2 and the last 2 chars
from a given a string. If the string length is less than 2, return instead of the
empty string.
Sample String : 'Python'
Expected Result : 'Pyon'
Sample String : 'Py'
Expected Result : 'PyPy'
Sample String : ' w'
Expected Result : Empty String'''

string=(input('Insert a word: '))

outstr=''
if len(string)<2:
    print('Empty string')
elif len(string)==2:
    outstr += string +string
    print(outstr)
else:
    outstr += string[:2]
    outstr += string[-2:]
    print(outstr)
