
from pymongo import MongoClient

#### trecho de código passível de erro
client = MongoClient()

collection = client.pessoa

documento = {
        'cpf': 22222,
        'nome': 'Lucas', 
        'idade': 22,
        'UF': 'SP'
        }


collection.pessoa.insert_one(documento)

### consulta

for documento in collection.pessoa.find():
    print(documento)
