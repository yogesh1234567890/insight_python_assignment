#38.​ Write a Python program to remove a key from a dictionary.

dict={'a':1,'b':2,'c':3}

try:
    del dict[input('Enter the key you want to remove: ')]
    print(dict)
except KeyError:
    print("That key is not available")