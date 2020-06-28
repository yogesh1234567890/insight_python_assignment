''' 4.​ Write a Python program to get a single string from two given strings, separated
by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz' '''

str1= 'abc'
str2= 'xyz'

out1 = str1.replace(str1[:2], str2[:2])
out2 = str2.replace(str2[:2], str1[:2])


output = out1 + ' ' + out2
print(output)