#19.​ Write a Python program to get the smallest number from a list.


input_string = input("Enter a list element separated by space: ")
list  = input_string.split()
list.sort()
print("The smallest number in the list is: " + str(list[0]))