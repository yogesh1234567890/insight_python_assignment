#16.​ Write a Python program to square and cube every number in a given list of
#integers using Lambda.


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in nums:
    square=lambda x:x*x
    cube=lambda x:x*x*x
    print("\nNow " + str(i)+" for square: ")

    print(square(i))
    print("\nNow " + str(i)+" for cube: ")
    print(cube(i))