import os
import json
import textwrap
def setPersonalData(name, caja):
    # 1. Leer el contenido actual del archivo JSON en una estructura de datos
    with open(os.path.join(os.getcwd(), "src", "data", "box_info.json"), "r", encoding='utf-8') as archivo:
        data = json.load(archivo)

    # 2. Modificar la estructura de datos (en este caso, supongamos que estamos agregando un nuevo campo)
    data['name']=name
    data['box']= caja

    # 3. Sobrescribir el archivo JSON con la nueva información
    with open(os.path.join(os.getcwd(), "src", "data", "box_info.json"), "w", encoding='utf-8') as archivo:
        json.dump(data, archivo)

def getBoxNum():
    with open(os.path.join(os.getcwd(), "src", "data", "box_info.json"), "r", encoding='utf-8') as file:
        box_num=json.load(file)
        return box_num['box']

def getName():
    with open(os.path.join(os.getcwd(), "src", "data", "box_info.json"), "r", encoding='utf-8') as file:
        name=json.load(file)
        return name['name']
    
def getLastNum():
    with open(os.path.join(os.getcwd(), "src", "data", "last_num.json"), "r", encoding='utf-8') as file:
        last_num=json.load(file)
        return last_num['num']

def getLastTime():
    with open(os.path.join(os.getcwd(), "src", "data", "last_num.json"), "r", encoding='utf-8') as file:
        last_hour=json.load(file)
        return last_hour['hour']
    

def getVideoPath():
    with open(os.path.join(os.getcwd(), "src", "data", "server_data.json"), "r", encoding='utf-8') as file:
        json_file= json.load(file)
        return f'''\\\\{json_file['IP']}\\videosTicketera\\'''

def getConnectionString():
    with open(os.path.join(os.getcwd(), "src", "data", "server_data.json"), "r", encoding='utf-8') as file:
        json_file= json.load(file)
        old_con_str = (
        r'DRIVER={SQL Server};'
        r'SERVER=GONZALO\DBGON;'
        r'DATABASE=turnos;'
        r'Trusted_Connection=yes;'
        )
        if (json_file['TRUSTED_CONNECTION']=='yes'):
            connection_string = (f"DRIVER={json_file['DRIVER']};"
                                f"SERVER={json_file['SERVER']};"
                                f"DATABASE={json_file['DATABASE']};"
                                f"Trusted_Connection={json_file['TRUSTED_CONNECTION']};")

        else:
            connection_string = (f"DRIVER={json_file['DRIVER']};"
                                f"SERVER={json_file['SERVER']};"
                                f"DATABASE={json_file['DATABASE']};"
                                f"USERNAME={json_file['USERNAME']};"
                                f"PASSWORD={json_file['PASSWORD']};")
        return connection_string