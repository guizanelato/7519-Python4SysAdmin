
from pymongo import MongoClient

#### trecho de código passível de erro
client = MongoClient()

collection = client.pessoa

collection.pessoa.update_one({'nome': 'Lucas'},
        {'$set' : {'UF': 'PE', 'nacionalidade': 'brasileira'}})

res = collection.pessoa.find_one({'nome':'Lucas'})

print(res)
