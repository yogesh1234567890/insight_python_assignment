''' 8. ​ Write a Python program to remove the n​ th​ index character from a nonempty
string.  '''


name=str(input('Enter a word: '))
index=int(input('Enter the index number to remove from the word: '))

namestr=[]
output=""
for i in range(len(name)):
    namestr.append(name[i])

for j in range(len(namestr)):
    if index ==j:
        namestr.pop(j)
        for val in namestr:
            output +=val
        print(output)



    