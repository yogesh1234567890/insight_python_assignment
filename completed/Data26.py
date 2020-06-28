""" 26.​ Write a Python program to insert a given string at the beginning of all items in
a list.
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']  """


Sample_list=[1,2,3,4]
string='emp'
output=[]
for value in Sample_list:
    value=string + str(value)
    output.append(value)

print(output)
    
