import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['food_recipes']
collection = database['food']

foods = collection.find({})

for food in foods:
    print(food)