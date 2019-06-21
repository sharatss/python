import re

# Search
if re.search("cat","A cat and a rat can't be friends."):
    print("cat found!!")
else:
    print("cat not found :(")


from urllib.request import urlopen
with urlopen('https://www.python-course.eu/simpsons_phone_book.txt') as fh:
    for line in fh:
        # line is a byte string so we transform it to utf-8:
        line = line.decode('utf-8').rstrip() 
        if re.search(r"J.*Neu",line):
            print(line)


mo = re.search("[0-9]+", "Customer number: 232454, Date: February 12, 2011")

# return the substring, which had been matched by the complete regular expression
print(mo.group())

# return the start and end of the matched substrings
print(mo.span())
print(mo.start())
print(mo.end())
