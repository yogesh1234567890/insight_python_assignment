#44.​ Write a Python program to slice a tuple.



lst=[]
num=int(input('Enter the num of values you want to keep in your tuple: '))
for i in range(num):
     val=input('Enter the tuple value: ')
     lst+=val
t=tuple(lst)
print(t)

s=int(input('Mention the starting point: '))
e=int(input('Mention the ending point: '))

print(t[s-1:e])
