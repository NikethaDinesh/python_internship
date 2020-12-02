import re
str=input("Enter string:")
pattern=re.search('[0-9]+$',str)
if pattern:
    print("matched")
else:
    print("not match")
