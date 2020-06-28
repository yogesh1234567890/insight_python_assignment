#45.​ Write a Python program to find the index of an item of a tuple.

tups=(1,2,3,4,5)
val=3
for vals in range(len(tups)):
    if tups[vals]==val:
        print("The index of " + str(val)+" is: "+ str(vals))
