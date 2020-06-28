""" 8.​ Write a Python function that takes a list and returns a new list with unique
elements of the first list.
Sample List : ​ [1,2,3,3,3,3,4,5]
Unique List : ​ [1, 2, 3, 4, 5]"""


def uniqlst(lis):
  x = []
  for a in lis:
    if a not in x:
      x.append(a)
  return x

print(uniqlst([1,2,3,3,3,3,4,5])) 
