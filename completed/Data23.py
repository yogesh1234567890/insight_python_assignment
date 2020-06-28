#23. ​ Write a Python program to check a list is empty or not.


list=[1,2,3]
count=0

for values in list:
    count +=1

if count==0:
    print("Empty list")
else:
    print('It has values')