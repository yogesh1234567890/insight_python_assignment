""" 2.​ Write a Python function to sum all the numbers in a list.
Sample List : ​ (8, 2, 3, 0, 7)
Expected Output ​ : 20 """

list=[8,2,3,0,7]




def sum(list):
    add=0
    for i in list:
        add+=i
    return add

print("The sum is: "+str(sum(list)))