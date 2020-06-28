'''  14.​ Write a Python function to create the HTML string with tags around the
word(s).
Sample function and result :add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>' '''

html=str(input("Enter a sentence: "))
tag=str(input("Enter a tag: "))


def add_tags(html, tag):
    return('<'+tag+'>' + html + '</'+tag+'>')

ans=add_tags(html,tag)
print(ans)