import win32print

def print_text(text, printer_name=None):
    # Obtener la impresora predeterminada si no se proporciona el nombre de la impresora
    if not printer_name:
        printer_name = win32print.GetDefaultPrinter()

    # Abrir una conexión con la impresora
    printer_handle = win32print.OpenPrinter(printer_name)

    # Especificar las opciones de impresión, como el tamaño de papel y la orientación
    default_printer_info = win32print.GetPrinter(printer_handle, 2)
    devmode = default_printer_info["pDevMode"]
    devmode.Orientation = win32print.DMORIENT_PORTRAIT  # Orientación vertical
    devmode.PaperSize = win32print.DMPAPER_A4  # Tamaño del papel A4
    win32print.DocumentProperties(0, printer_handle, printer_name, devmode, devmode, 0)
    try:
        # Iniciar el trabajo de impresión
        job_info = win32print.StartDocPrinter(printer_handle, 1, (text, None, "RAW"))

        # Escribir el contenido del texto en el trabajo de impresión
        win32print.WritePrinter(printer_handle, text.encode())

        # Finalizar el trabajo de impresión
        win32print.EndPagePrinter(printer_handle)
        win32print.EndDocPrinter(printer_handle)

        print("¡Impresión exitosa!")
    except Exception as e:
        print(f"Error al imprimir: {e}")
    finally:
        # Cerrar la conexión con la impresora
        win32print.ClosePrinter(printer_handle)

# Texto que deseas imprimir
texto_a_imprimir = "¡Hola desde Python! Este es un texto de prueba para imprimir."

# Llamar a la función para imprimir el texto
print_text(texto_a_imprimir)