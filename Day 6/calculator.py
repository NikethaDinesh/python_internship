num1=float(input("enter num1:"))
num2=float(input("enter num2:"))
res=0
operator=input("enter operator:")

if(operator=="+"):
    res=num1+num2
if(operator=="-"):
    res=num1-num2
if(operator=="*"):
    res=num1*num2
if(operator=="/"):
    res=num1/num2
print("output:",res)