import logging

#SOLO IMPORTANDO YA CARGA CONFIGURACION
logging.basicConfig(level=logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('C:/Ticketera/log_info.log')
file_handler.setFormatter(formatter)
logging.getLogger('').addHandler(file_handler)


'''
# Registra algunos mensajes en tu código
logging.debug("Este es un mensaje de depuración.")
logging.info("Este es un mensaje informativo.")
logging.warning("Este es un mensaje de advertencia.")
logging.error("Este es un mensaje de error.")
logging.critical("Este es un mensaje crítico.")
'''