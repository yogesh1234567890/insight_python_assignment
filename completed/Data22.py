#22. ​ Write a Python program to remove duplicates from a list.

mylist=[1,2,3,4,5,4,3,2]
mylist = list(dict.fromkeys(mylist))
print(mylist)
##here the list is converted into dictionaries by which all duplicates are removed and its well again converted back to list