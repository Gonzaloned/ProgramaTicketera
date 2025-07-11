const Printer = require('node-thermal-printer').printer;
const Types = require('node-thermal-printer').Types;

// Configuración de la impresora
const printer = new Printer({
  type: Printer.TYPE.EPSON, // Tipo de impresora térmica (puede variar según tu impresora)
  interface: 'EPSON TM-T88V Receipt' // Nombre de la impresora (puedes encontrarlo en la configuración de tu sistema)
});

// Texto a imprimir
const textToPrint = `
¡Hola, mundo!
Este es un ejemplo de impresión térmica desde JavaScript.
`;

// Inicializar la impresora
printer.init();

// Añadir el texto a la cola de impresión
printer.alignCenter();
printer.setTextQuadArea();
printer.setTextDoubleHeight();
printer.setTextDoubleWidth();
printer.println(textToPrint);

// Finalizar y enviar la impresión
printer.cut();
printer.execute();

// Manejo de errores
printer.on('error', (err) => {
  console.error('Error de impresión:', err);
});
