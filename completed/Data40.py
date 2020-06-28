#40.​ Write a Python program to add an item in a tuple.

tups=(1,2,3,4,5,6,7,8)
lst=list(tups)
num=int(input("Enter the number of values you want to add in the tuple: "))

for i in range(num):
    value=int(input('Enter the value: '))
    lst.append(value)

out=tuple(lst)
print(out)