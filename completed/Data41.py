#41.​ Write a Python program to convert a tuple to a string.


tups=(1,2,3,4,5,6,7,8)
lst=list(tups)
strs=''
for values in lst:
    strs +=str(values)

print(strs)

