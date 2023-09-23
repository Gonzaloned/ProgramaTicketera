const ThermalPrinter = require("node-thermal-printer").printer;
const PrinterTypes = require("node-thermal-printer").types;

//save in args the list of strings
const args = process.argv.slice(2);

async function imprimirTicket() {
  let printer = new ThermalPrinter({
    type: PrinterTypes.EPSON,
    interface: '//localhost/printer'
  });
  

  printer.setTextSize(1,1)
  console.log('Argumentos recibidos:', args);
  printer.alignCenter();
  printer.println(args[0]);
  printer.println(args[1]);
  printer.println("Hello world");

  try {
    // Usar await dentro de una función async
    await printer.printImage('logo2.png')
    printer.cut();
    
    let execute = printer.execute()
    console.log("Print done!");
  } catch (error) {
    console.error("Print failed:", error);
  }
}

// Llamar a la función async para imprimir el ticket
imprimirTicket();
