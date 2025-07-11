from escpos.printer import Usb
import usb.core
""" Seiko Epson Corp. Receipt Printer M129 Definitions (EPSON TM-T88IV) """
p = Usb(0x04b8,0x0e020,0)
p.text("Hello World\n")
p.image("logo.gif")
p.barcode('1324354657687','EAN13',64,2,'','')
p.cut()

