#30.​ Write a Python script to check whether a given key already exists in a dictionary.
dicts={}
data=int(input("Enter the number of dictionaries values: "))
for i in range(data):
    k=input("Enter the key: ")
    v=input("Enter the value: ")
    dicts.update({k:v})

userkey=input("Enter the element to check: ")

for key,value in dicts.items():
    if key==userkey:
        print(str(key) +" exists in dictionary with "+str(value) +" value")

print(dicts)    