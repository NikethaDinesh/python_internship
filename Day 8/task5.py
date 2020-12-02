try:
    lst=[]
    n=int(input("Enter n:"))
    for i in range (0,n):
       value=int(input())
       lst.append(value)
    print(lst)
    print("enter index to be popped:")
    pop_ind=int(input())
    lst.pop(pop_ind)
    print(lst)
except Exception as e:
    print(e)
