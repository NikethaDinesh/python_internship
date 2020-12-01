lst=[3,23,4,5,6,75,88,19,56,43,89]
count=0
lst2=list(filter(lambda x:x%2==0,lst))
print("count of even nos. in the list:",len(lst2))