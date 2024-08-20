from pymongo import MongoClient

def criar_banco(nome_cliente, nome_db, data):
    client = MongoClient('mongodb://localhost:27017/')
    db = client[nome_cliente]
    new_collection = db[nome_db]
    new_collection.insert_one(data)
    print("Banco de dados e coleção criados com sucesso!")
