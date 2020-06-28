'''  15.​ Write a Python function to insert a string in the middle of a string.
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}} '''

def insert_func(tag,word):
    return tag[:2] + word + tag[2:]

print(insert_func('[[]]','python'))

