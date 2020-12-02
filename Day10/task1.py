import re
str=input("enter string:")
pattern=re.compile("[A-Za-z0-9]+")
if pattern.fullmatch(str) :
    print("matched")
else:
    print("Not match")
