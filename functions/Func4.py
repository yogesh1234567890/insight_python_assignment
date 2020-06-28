""" 4.​ Write a Python program to reverse a string.
Sample String ​ : "1234abcd"
Expected Output ​ : "dcba4321" """

str="1234abcd"

def reverse(str):
    rev=str[::-1]
    print(rev)

reverse(str)