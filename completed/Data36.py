#36.​ Write a Python program to sum all the items in a dictionary.

dicts={}
data=int(input("Enter the number of dictionaries values: "))
for i in range(data):
    k=input("Enter the key: ")
    v=int(input("Enter the value: "))
    dicts.update({k:v})

print("The sum of values is: "+sum(dicts.values()))