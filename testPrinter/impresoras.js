const Printer = require('node-thermal-printer').printer;
const Types = require('node-thermal-printer').Types;

const printer = new Printer();

// Listar las impresoras disponibles
const printerList = printer.getPrinters();
console.log('Impresoras disponibles:', printerList);

// Configuración de la impresora
if (printerList.length > 0) {
  const selectedPrinter = printerList.find(printer => printer.name === 'EPSON TM-T88V Receipt');

  if (selectedPrinter) {
    const selectedPrinterName = selectedPrinter.name;

    const configuredPrinter = new Printer({
      type: Types.EPSON, // Tipo de impresora térmica Epson
      interface: 'printer:' + selectedPrinterName, // Nombre de la impresora
      options: {
        timeout: 5000 // Tiempo de espera en milisegundos para la conexión (puede ajustarse según sea necesario)
      }
    });

    // Texto a imprimir
    const textToPrint = `
    ¡Hola, mundo!
    Este es un ejemplo de impresión térmica desde JavaScript en una impresora Epson.
    `;

    // Inicializar la impresora
    configuredPrinter.isPrinterConnected((isConnected) => {
      if (isConnected) {
        configuredPrinter.init();

        // Añadir el texto a la cola de impresión
        configuredPrinter.alignCenter();
        configuredPrinter.setTextQuadArea();
        configuredPrinter.setTextDoubleHeight();
        configuredPrinter.setTextDoubleWidth();
        configuredPrinter.println(textToPrint);

        // Finalizar y enviar la impresión
        configuredPrinter.cut();
        configuredPrinter.execute();

        // Manejo de errores
        configuredPrinter.on('error', (err) => {
          console.error('Error de impresión:', err);
        });
      } else {
        console.error('No se pudo conectar a la impresora.');
      }
    });
  } else {
    console.error('La impresora "EPSON TM-T88V Receipt" no está disponible.');
  }
} else {
  console.error('No se encontraron impresoras disponibles.');
}