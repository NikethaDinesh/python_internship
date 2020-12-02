import re
str=input("Enter string:")
if re.search('ab',str):
    print("matched")
else:
    print("no matches")
