import os
import json
def obtener_ultima_partida():
    '''Abre el archivo json que contiene la información de la ultima sesion, y retorna un diccionario. En caso de no existir, lo crea con valores por defecto'''
    try:
        with open(os.path.join(os.getcwd(), "src", "datos", "ultima_partida.json"), "r", encoding='utf-8') as partida:
            ultima_partida = json.load(partida)
    except:
        with open(os.path.join(os.getcwd(), "src", "datos", "ultima_partida.json"), "w", encoding='utf-8') as partida:
            ultima_partida = {"nick": "Sin datos", "dificultad": "Sin datos", "fecha": "Sin datos", "puntaje": "Sin datos"}
            json.dump(ultima_partida, partida)
    return ultima_partida

def obtenerCaja():
    '''Abre el archivo json y si no existe lo crea'''
    try:
        with open(os.path.join(os.getcwd(), "src", "datos", "info_caja.json"), "r", encoding='utf-8') as caja:
            datos_caja = json.load(caja)
    except:
        with open(os.path.join(os.getcwd(), "src", "datos", "info_caja.json"), "w", encoding='utf-8') as caja:
            datos_default= {'nombre':'undefined','caja':'1'}
            datos_caja = json.dump(caja)
    return datos_caja
