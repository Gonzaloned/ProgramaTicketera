import os
import json

def setPersonalData(nombre, caja):
    # 1. Leer el contenido actual del archivo JSON en una estructura de datos
    with open(os.path.join(os.getcwd(), "src", "data", "info_caja.json"), "r", encoding='utf-8') as archivo:
        data = json.load(archivo)

    # 2. Modificar la estructura de datos (en este caso, supongamos que estamos agregando un nuevo campo)
    data['nombre']=nombre
    data['caja']= caja

    # 3. Sobrescribir el archivo JSON con la nueva información
    with open(os.path.join(os.getcwd(), "src", "data", "info_caja.json"), "w", encoding='utf-8') as archivo:
        json.dump(data, archivo)

def getBoxNum():
    with open(os.path.join(os.getcwd(), "src", "data", "info_caja.json"), "r", encoding='utf-8') as file:
        box_num=json.load(file)
        return box_num['caja']

def getName():
    with open(os.path.join(os.getcwd(), "src", "data", "info_caja.json"), "r", encoding='utf-8') as file:
        name=json.load(file)
        return name['nombre']