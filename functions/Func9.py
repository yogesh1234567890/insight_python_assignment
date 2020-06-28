""" 9.​ Write a Python function that takes a number as a parameter and check the
number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that
has no positive divisors other than 1 and itself. """

val=int(input("Enter a number: "))
def prime(num):
    if num>1:
        for i in range(2,num):
            if num%i ==0:
                print("This is not a prime number")
                break
            else:
                print("Yes, this is prime")
                break
    else:
        print("value should be greater than one")

prime(val)