""" 32.​ Write a Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} """

n=int(input('Enter the number: '))
output={}

for i in range(n+1):
    if i ==0:
        continue
    k=i
    v=i*i
    output.update({k:v})

print(output)