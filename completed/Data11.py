''' 11. ​ Write a Python program to count the occurrences of each word in a given
sentence.  '''

sentence=str(input('Enter a sentence: '))
import collections
sent=[]

x=sentence.split(' ')
sent +=x
frequencies=collections.Counter(sent)
repeated = {}

for key, value in frequencies.items():
    if value >=0:
        repeated[key] = value

print(repeated)