#14.​ Write a Python program to sort a list of dictionaries using Lambda.

models = [{'name':'yogesh', 'age':19, 'sex':'male'},{'name':'Rahsit', 'age':70, 'sex':'male'}, {'name':'Kim', 'age':29, 'sex':'female'},]
print("Original list:")
print(models)
sorted_models = sorted(models, key = lambda x: x['name'])
print("\nSorting the List on name basis::")
print(sorted_models)

sorted_models = sorted(models, key = lambda x: x['age'])
print("\nSorting the List on age basis::")
print(sorted_models)
