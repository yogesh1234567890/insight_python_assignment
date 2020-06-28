''' 9. ​ Write a Python program to change a given string to a new string where the first
and last chars have been exchanged.  '''


def change_sring(word):
      return name[-1:] + name[1:-1] + name[:1]

name=input('Enter a word which you want to process: ')
ans=change_sring(name)
print(ans)