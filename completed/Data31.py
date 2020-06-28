#31.​ Write a Python program to iterate over dictionaries using for loops.

d = {'name':'ram', 'age': 12, 'sex':'male','job':'study'} 
for key, value in d.items():
     print(key, 'related to ', d[key]) 