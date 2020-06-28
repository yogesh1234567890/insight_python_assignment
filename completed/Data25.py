""" 25.​ Write a Python program to check whether all dictionaries in a list are empty or
not.
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False """

empt_dict=[{},{},{}]
nonempt_dict=[{1,2},{},{}]

print(all(not value for value in empt_dict))
print(all(not value for value in nonempt_dict))
