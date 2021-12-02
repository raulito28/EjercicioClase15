import pickle

def store(data, filename):
    pickle.dump(data, open(filename, "wb"))

def retrieve(filename):
    try:
        archivo = open(filename, "rb" )
    except:
        print("Error al abrir el archivo", filename)
        return None

    content = pickle.load(archivo)
    archivo.close()
    return content