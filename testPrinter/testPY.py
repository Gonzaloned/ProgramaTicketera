import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def print_ticket_automatically():
    # Configurar las opciones del navegador Chrome para que no muestre la ventana
    '''chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')'''

    # Inicializar el navegador Chrome
    driver = webdriver.Chrome()#options=chrome_options)

    # Cargar el contenido del ticket HTML en el navegador
    ticket_url = 'C:/Users/gon/Desktop/testPrinter/ticket.html'
    driver.get(ticket_url)
    time.sleep(2)

    ticket_height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
    print(ticket_height)
    # Establecer el tamaño de papel personalizado para que se ajuste al contenido del ticket
    #devmode = driver.execute_async_script("var callback = arguments[arguments.length - 1]; window.matchMedia('print').addListener(function(mql) { if (mql.matches) { callback({paperSize: {width: '100mm', height: '%spx', margin: '0'}}); }});" % ticket_height)

    # Configurar las opciones de impresión con el tamaño de papel personalizado
    driver.execute_script("Object.assign(document.body.style, {'width': '100mm', 'height': '%spx', 'margin': '0'})" % ticket_height)

    # Simular el proceso de impresión mediante atajos de teclado
    pyautogui.hotkey('ctrl', 'p')
    time.sleep(2)  # Asegurar tiempo suficiente para que se abra la ventana de impresión
    print("enter")
    # Simular la presión de la tecla Enter para iniciar la impresión
    #pyautogui.press('enter')

    # Esperar un momento para que la impresión se complete (ajusta el tiempo según tu sistema)
    time.sleep(5)

    # Cerrar el navegador
    driver.quit()

# Llamar a la función para imprimir el ticket automáticamente
print_ticket_automatically()