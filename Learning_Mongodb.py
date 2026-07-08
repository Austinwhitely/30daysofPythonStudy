# %%
from flask import Flask, render_template
import os
import pymongo
from bson.objectid import ObjectId

# %%
MONGODB_URI = (
    "mongodb+srv://austinwhitely1:Pornhubaddict10!@30daysofpython.h7o6zcf.mongodb.net/"
)
client = pymongo.MongoClient(MONGODB_URI)


db = client.thirty_days_of_python  # Creating database

db.students.insert_one(
    {"name": "Asabeneh", "country": "Finland", "city": "Helsinki", "age": 250}
)  # Creating students collection and inserting a document

db.students.insert_many(
    [
        {"name": "David", "country": "UK", "city": "London", "age": 34},
        {"name": "John", "country": "Sweden", "city": "Stockholm", "age": 28},
        {"name": "Sami", "country": "Finland", "city": "Helsinki", "age": 25},
    ]
)
# %%
print(client.list_database_names())

# %%

student = db.students.find_one()
print(student)

student = db.students.find_one({"_id": ObjectId("6a4e8b300bdead01d82ddf8e")})
print(student)

students = db.students.find(
    {}, {"_id": 0, "name": 1, "country": 1}
)  # 0 means not include and 1 means include
for student in students:
    print(student)
# %%

# GETTING QUERIES
query = {"country": "Finland"}

students = db.students.find(query)
for student in students:
    print(student)

query = {"age": {"$gt": 30}}

students = db.students.find(query)
for student in students:
    print(student)

students = db.students.find().limit(3)
for student in students:
    print(student)
# %%

# SORTING
students = db.students.find().sort("name")
for student in students:
    print(student)


students = db.students.find().sort("name", -1)
for student in students:
    print(student)

students = db.students.find().sort("age")
for student in students:
    print(student)

students = db.students.find().sort("age", -1)
for student in students:
    print(student)

# %%
# UPDATING AND DELETING

query = {"age": 250}
new_value = {"$set": {"age": 38}}

db.students.update_one(query, new_value)

for student in db.students.find():
    print(student)

query = {"name": "John"}
db.students.delete_one(query)

for student in db.students.find():
    print(student)


db.students.drop()  # DROPS WHOLE COLLECTION

app = Flask(__name__)
if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

# %%
