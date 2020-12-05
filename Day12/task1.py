import json
from pymongo import MongoClient


x={
    "name":"sehun",
    "age":27,
    "gender":"male",
    "fee payment":True,
    "course":["IOT","ML"]
  },{"name":"suho",
    "age":25,
    "gender":"male",
    "fee payment":True,
    "course":["TQM","ML"]
  }
with open("stud.json","w")as f:
    json.dump(x,f,indent=5)

myclient=MongoClient("mongodb://localhost:27017/")
db=myclient["traineedb"]
Collection=db["trainee"]
with open("stud.json")as f:
    data=json.load(f)
if isinstance(data,list):
    Collection.insert_many(data)
else:
    Collection.insert_one(data)