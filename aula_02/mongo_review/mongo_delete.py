
from pymongo import MongoClient

#### trecho de código passível de erro
client = MongoClient()

collection = client.pessoa

collection.pessoa.delete_one({'nome': 'Lucas'})

for item in collection.pessoa.find():
    print(item)
