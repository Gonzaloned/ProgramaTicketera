import win32print
import win32ui
from PIL import Image, ImageWin

TICKET_WIDTH = 300  # Ancho deseado del ticket en puntos (1 pulgada = 72 puntos)
PHYSICALWIDTH = 110
PHYSICALHEIGHT = 111

printer_name = win32print.GetDefaultPrinter()
print(printer_name)
file_name = "C:/Users/gon/Desktop/Ticketera/img/logo.jpeg"

hDC = win32ui.CreateDC()
hDC.CreatePrinterDC(printer_name)
printer_size = hDC.GetDeviceCaps(PHYSICALWIDTH), hDC.GetDeviceCaps(PHYSICALHEIGHT)

print(printer_size)

bmp = Image.open(file_name)

# Redimensionar la imagen manteniendo la relación de aspecto original
print("Tamaño original de la imagen:", bmp.size(50,50))

# Redimensionar la imagen manteniendo la relación de aspecto original
bmp = bmp.resize((50, 50))

print("Tamaño redimensionado de la imagen:", bmp.size)


#if bmp.size[0] < bmp.size[1]:
#    bmp = bmp.rotate(90)

hDC.StartDoc(file_name)
hDC.StartPage()

dib = ImageWin.Dib(bmp)
dib.draw(hDC.GetHandleOutput(), (0, 0, printer_size[0], printer_size[1]))

hDC.EndPage()
hDC.EndDoc()
hDC.DeleteDC()
