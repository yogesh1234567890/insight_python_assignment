""" 7.​ Write a Python function that accepts a string and calculate the number of
upper case letters and lower case letters.Sample String ​ : 'The quick Brow Fox'
Expected Output : ​
No. of Upper case characters : 3
No. of Lower case Characters : 12 """

string="The quick Brow Fox"

def check(string):
    upper=0
    lower=0
    for i in range(len(string)):
        if ord(string[i])>=97 and ord(string[i])<=122:
            lower+=1
        else:
            if ord(string[i])==32:
                continue
            upper+=1
    print("No. of Upper case characters: "+str(upper))
    print("No. of Lower case characters: "+str(lower))
    

check(string)