#write a python program to find intersection of two given arrays using lambda.

array1=[1,2,3,4,5,6,7,8,9]
array2=[-5,1,3,5,7,9,11,15]

intersection=list(filter(lambda x:x in array1,array2))
print("The intersection of two arrays are: ",intersection)