from math import cube       #import error

import cube         #module not found error

stud={1:"loey",2:"bbh",3:"kai"}
print(stud[4])      #key error

list1=[90,40,45]
print(list1[3])     #index error

marks=max(list1)
if marks<40:
    div=marks/0     #Zerodivision error
    print(div)
elif marks>40 | marks<80 :
    div=marks/2
    print(div)
else                #syntax error
    div=marks
    print(div)

print(name)         #name error

age=2
print('age'+2)      #type error

