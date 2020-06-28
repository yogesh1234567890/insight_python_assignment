'''3. ​ Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t' '''

user=input("Enter a word: ")
def replace_fun(val):
    char=val[0]
    val=val.replace(char,'$')
    val=char + val[1:]
    return val

print(replace_fun(user))