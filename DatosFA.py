from pymongo.mongo_client import MongoClient
    
uri = "mongodb+srv://fabioandrestdea:1234@cluster0.6pgb67o.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

try:
    client.admin.command('ping')    
    db = client["FarmaApp"]
    collection = db["Usuarios"]

except Exception as e:
    print(e)

def agregar_usuario(usuario):    
    result = collection.insert_one(usuario)
    inserted_id = result.inserted_id    

def buscar_usuario(usuario):
    filtro = {'nombre': usuario}
    resultado = collection.find_one(filtro)
    return resultado
        


