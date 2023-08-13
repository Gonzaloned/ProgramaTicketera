import win32print
import win32ui

 
from PIL import Image, ImageDraw, ImageFont, ImageWin

def Impresion(texto1, num1, logo, texto2, printer_name):
    # Tamaño del papel en puntos (1 pulgada = 72 puntos)
    PAGE_WIDTH = 8.5 * 72
    PAGE_HEIGHT = 11 * 72

    # Tamaño del margen
    MARGIN = 0.5 * 72

    # Tamaño del título
    TITLE_SIZE = 36

    # Tamaño del número
    NUMBER_SIZE = 24

    # Tamaño del pie de página
    FOOTER_SIZE = 12

    try:  
        hDC = win32ui.CreateDC ()
        hDC.CreatePrinterDC (printer_name)
        printer_size = hDC.GetDeviceCaps (PAGE_WIDTH), hDC.GetDeviceCaps (PAGE_HEIGHT)

        # Crear una imagen blanca del tamaño de la página
        bmp = Image.new("RGB", (printer_size[0], printer_size[1]), "white")

        # Abrir la imagen del logo
        logo_image = Image.open(logo)
        logo_image = logo_image.resize((int(logo_image.width * 0.5), int(logo_image.height * 0.5)))

        # Agregar el logo al centro de la página
        x_logo = int((PAGE_WIDTH - logo_image.width) / 2)
        y_logo = int((PAGE_HEIGHT - logo_image.height) / 2)
        bmp.paste(logo_image, (x_logo, y_logo))

        # Crear un objeto Draw para dibujar en la imagen
        draw = ImageDraw.Draw(bmp)

        # Fuente para el título
        title_font = ImageFont.truetype("arial.ttf", TITLE_SIZE)

        # Obtener el tamaño del título
        title_width, title_height = draw.textsize(texto1, title_font)

        # Calcular la posición para centrar el título en la página
        x_title = int((PAGE_WIDTH - title_width) / 2)
        y_title = y_logo - title_height - MARGIN

        # Agregar el título al centro de la página
        draw.text((x_title, y_title), texto1, font=title_font, fill="black")

        # Fuente para el número
        number_font = ImageFont.truetype("arial.ttf", NUMBER_SIZE)

        # Obtener el tamaño del número
        num_width, num_height = draw.textsize(str(num1), number_font)

        # Calcular la posición para centrar el número en la página
        x_num = int((PAGE_WIDTH - num_width) / 2)
        y_num = y_logo + logo_image.height + MARGIN

        # Agregar el número al centro de la página
        draw.text((x_num, y_num), str(num1), font=number_font, fill="black")

        # Fuente para el pie de página
        footer_font = ImageFont.truetype("arial.ttf", FOOTER_SIZE)

        # Obtener el tamaño del pie de página
        footer_width, footer_height = draw.textsize(texto2, footer_font)

        # Calcular la posición para centrar el pie de página en la página
        x_footer = int((PAGE_WIDTH - footer_width) / 2)
        y_footer = PAGE_HEIGHT - footer_height - MARGIN

        # Agregar el pie de página al centro de la página
        draw.text((x_footer, y_footer), texto2, font=footer_font, fill="black")

        # Iniciar el documento y la página de impresión
        hDC.StartDoc("ImpresionPersonalizada")
        hDC.StartPage()

        # Dibujar la imagen en el contexto de impresora
        dib = ImageWin.Dib(bmp)
        dib.draw(hDC.GetHandleOutput(), (0, 0, printer_size[0], printer_size[1]))

        # Finalizar la página y el documento de impresión
        hDC.EndPage()
        hDC.EndDoc()

        # Eliminar el objeto DC
        hDC.DeleteDC()

        print("Impresión exitosa")

    except Exception as e:
        print("Error al imprimir:", e)

# Llamar a la función para imprimir con datos personalizados
printer_name = win32print.GetDefaultPrinter ()
texto1 = "Título grande centrado"
num1 = 123456
logo = "ruta_de_la_imagen.jpg"
texto2 = "Pie de página con letra chica"


Impresion(texto1, num1, logo, texto2, printer_name)