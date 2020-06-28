#43.​ Write a Python program to remove an item from a tuple.

tups=(1,2,3,4,5,6)
lst=list(tups)
try:
    val=int(input("Enter the item you want to remove: "))
    out=lst.pop(val-1)
    print(lst)
except:
    print("The value you entered is not available")