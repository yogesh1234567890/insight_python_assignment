#17.​ Write a Python program to find if a given string starts with a given character using Lambda.


string='python'
char='p'
starts_with = lambda x: True if x.startswith(char) else False
print(starts_with(string))

