#34.​ Write a Python script to merge two Python dictionaries.

dict1={'a':1,'b':2,'c':3}
dict2={'d':4,'e':5,'f':6}

dict={}

def merge(dict1,dict2):

    dict.update(dict1)
    dict.update(dict2)
    return dict

out=merge(dict1,dict2)
print(out)
