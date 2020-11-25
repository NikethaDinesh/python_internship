courses={"IOT":2,"MachineLearning":2,"TQM":1}
names={"loey":45,"sehun":30,"kai":44}
merge_dict= courses.copy()
merge_dict.update(names)   #merge 2 dictionaries
print(merge_dict)

key="TQM"
if(key) in courses : courses.pop(key)  #deletes key if present
print(courses)

keys=["name","age","Dept"]
values=["chen",28,"Music"]
final_dict=dict(zip(keys,values))   #map 2 list into a dictionary
print(final_dict)

department1={"CSE","ECE","EEE","CIVIL"}
print(len(department1))              #length of set

department2={"EEE","ME","Marine","CSE"}
print(department1-department2)          #removes intersecton of 2nd set from 1st


