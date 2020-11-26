marks=[50,45,47]
marks.append(48)    #adds item to end of list
print(marks)

marks.remove(47)       #deletes an item
print(marks)

max_mark=max(marks)
min_mark=min(marks)
print(max_mark , min_mark)      #max and min no. from list

age=(12,15,20,9)
rev_tuple=tuple(reversed(age))      #reversing tuple
print(rev_tuple)

fruits=("mango","orange","apple")
list_fruits=list(fruits)        #tuple to list conversion
print(list_fruits)
