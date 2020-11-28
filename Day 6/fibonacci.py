num=int(input("enter value for num:"))
n1,n2=0,1
count=0
if(num<=0):
    print("error! needs positive number")
elif(num==1):
    print(n1)
else:
    while(count<num):
        print(n1," " ,end="")
        n=n1+n2
        n1=n2
        n2=n
        count+=1