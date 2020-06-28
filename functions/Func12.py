""" 12.​ Write a Python program to create a function that takes one argument, and
that argument will be multiplied with an unknown given number.
""" 

def compute(n):
     return lambda x : x * n
result = compute(2)
print("Double the number of 10 =", result(10))

result = compute(3)
print("computing the number of 20 =", result(20))
