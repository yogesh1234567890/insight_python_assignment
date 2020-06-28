''' 6.​ Write a Python program to find the first appearance of the substring 'not' and
'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'  '''

string1='The lyrics is not that poor!'
'The lyrics is poor!'

def not_poor(str1):
    s_not=str1.find('not')
    s_poor=str1.find('poor')

    if s_poor >s_not and s_not >0 and s_poor>0:
        str1=str1.replace(str1[s_not:(s_poor+4)],'good')
        return str1
    
    else:
        return str1

print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))