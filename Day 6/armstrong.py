""" number is equal to sum fo cubes od its own digits ; 153=1^3+5^3=3^3"""
num=int(input("enter num:"))
sum=0
temp=num
while(temp>0):
    d=temp%10
    sum+=d ** 3
    temp //=10
if(num==sum):
    print("number is armstrong number")
else:
    print("not an armstrong number")
