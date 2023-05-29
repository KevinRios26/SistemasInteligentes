from pymongo.mongo_client import MongoClient



# uri = "mongodb+srv://nanitave:inteligy@cluster0.cn1aiyy.mongodb.net/farmaapp?retryWrites=true&w=majority"

# client = MongoClient(uri)

#  # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
#     db=client["FarmaApp"]
#     datos=db["Farmacia"]
#     for documento in datos.find():
#         print(documento)

# except Exception as e:
#     print(e)


    
uri = "mongodb+srv://fabioandrestdea:1234@cluster0.6pgb67o.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB! a Usuarios")

    db = client["FarmaApp"]
    collection = db["Usuarios"]

except Exception as e:
    print(e)

def agregar_usuario(usuario):    
    result = collection.insert_one(usuario)
    inserted_id = result.inserted_id
    print('Usuario insertado con ID:', inserted_id)

def buscar_usuario(usuario):
    filtro = {'nombre': usuario}
    resultado = collection.find_one(filtro)
    return resultado
        


