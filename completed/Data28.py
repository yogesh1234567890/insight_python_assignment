""" 28. ​ Write a Python script to add a key to a dictionary.Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30} """

dic={0:10,1:20}

val=int(input("Enter the number of keys you want to add: "))


for i in range(val):
    k=input("Enter key: ")
    v=input("Enter value: ")
    dic.update({k:v})

print(dic)