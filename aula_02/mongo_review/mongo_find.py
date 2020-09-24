
from pymongo import MongoClient

#### trecho de código passível de erro
client = MongoClient()

collection = client.pessoa

#busca restrita a um documento
res = collection.pessoa.find_one({'nome': 'Lucas'})

print(res)

#busca um ou mais registros:
for documento in collection.pessoa.find({'UF':'SP'}):
    print(documento)
