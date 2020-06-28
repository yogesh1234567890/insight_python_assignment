""" 3.​ Write a Python function to multiply all the numbers in a list.
Sample List : ​ (8, 2, 3, -1, 7)
Expected Output ​ : -336 """

list=[8,2,3,-1,7]

def prod(list):
    mul=1
    for i in list:
        mul*=i
    return mul

print("The multiplied value is: "+str(prod(list)))