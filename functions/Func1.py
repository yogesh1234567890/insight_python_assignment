#1.​ Write a Python function to find the Max of three numbers.

def max(*vals,**kvals):
    lst=[]
    lst+=vals
    sorted=lst.sort()
    return lst[-1]


a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))

ans=max(a,b,c)
print("The max of three numbers is: "+str(ans))
