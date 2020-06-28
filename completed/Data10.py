''' 10. ​ Write a Python program to remove the characters which have odd index
values of a given string.  '''

name=str(input('Enter a word: '))
out=''
for  i in range(len(name)):
    if i%2!=0:
        out += name[i]

print(out)