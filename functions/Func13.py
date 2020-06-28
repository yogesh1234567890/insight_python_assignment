#13.​ Write a Python program to sort a list of tuples using Lambda.

tup_list=[('Ram',100),('Hari',20),('Shyam',50)]

print(tup_list)
tup_list.sort(key=lambda x:x[1])
print(tup_list)