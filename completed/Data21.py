""" 21.​ Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""

def last_element(num):
    return num[-1]

def sort_list(first_element):
    return sorted(first_element, key=last_element)

print(sort_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))