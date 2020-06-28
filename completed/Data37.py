#37.​ Write a Python program to multiply all the items in a dictionary.

dicts={}
data=int(input("Enter the number of dictionaries values: "))
for i in range(data):
    k=input("Enter the key: ")
    v=int(input("Enter the value: "))
    dicts.update({k:v})

out=1
for keys,values in dicts.items():
    out*=dicts[keys]

print("The multiplied output is: "+out)