''' 5.​ Write a Python program to add 'ing' at the end of a given string (length should
be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'  '''

string=input('Enter a word: ')
output=''
if len(string)>=3:
    if string[3:]=='ing':
        output += string + 'ly'
        print(output)
    else:
        output +=string + 'ing'
        print(output)


