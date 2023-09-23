
# Ejecuta el script de Node.js desde Python
import subprocess


printer_file= 'ticketera.js'

#Parameters
param_list=['num','ticket']
try:
    subprocess.run(['node', printer_file, *param_list], check=True)
    print("Script de Node.js ejecutado con éxito desde Python.")
except subprocess.CalledProcessError as e:
    print("Error al ejecutar el script de Node.js:", e)
except FileNotFoundError:
    print("File not found")