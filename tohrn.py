import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb+srv://Jakkrathorn:Bouya4710@finalproject.nt7cb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.store
supply = db.supply
customers = db.customer
orders = db.order

results = orders.find({})
for data in results:
    print(data)