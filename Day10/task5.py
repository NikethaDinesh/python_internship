import re
str=input("Enter string:")
pattern=re.compile('^[A-Z]+$')
if pattern.findall(str):
    print("matched")
else:
    print("not match")