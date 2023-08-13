from escpos.printer import Usb

def print_text_on_epson_tm88v(text):
    try:
        # Crea una instancia de la impresora USB. Asegúrate de que el ID del dispositivo sea correcto.
        # Puedes encontrar el ID correcto ejecutando: lsusb en Linux o Mac, o Device Manager en Windows.
        printer = Usb(0x04b8, 0x0202, 0, 0x81, 0x03)

        # Establece el tamaño y la alineación del texto (opcional)
        printer.set(align='center', width=2, height=2)

        # Imprime el texto
        printer.text(text)

        # Corta el papel (opcional)
        printer.cut()

        # Cierra la conexión con la impresora
        printer.close()

        print("Impresión exitosa.")

    except Exception as e:
        print("Error al imprimir:", str(e))

# Llamada a la función para imprimir un texto
texto_a_imprimir = "¡Hola, esto es un ejemplo de impresión en la EPSON TM-T88V!"
print_text_on_epson_tm88v(texto_a_imprimir)
