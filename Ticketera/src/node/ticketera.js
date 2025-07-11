const ThermalPrinter = require("node-thermal-printer").printer;
const PrinterTypes = require("node-thermal-printer").types;

//save in args the list of strings
const args = process.argv.slice(2);
let printer = new ThermalPrinter({
  type: PrinterTypes.EPSON,
  interface: '//localhost/printer'
});

async function checkImpresora() {
  try{
  let isConnected = await printer.isPrinterConnected();
  if (isConnected){
    return true;
  }
  else{
    return false;
  }

  } catch (error){
  console.log("Error al verificar la imrpesora:", error);
  }

};



async function imprimirTicket() {

  
  num= args[0]
  type= args[1]
  printer.setTextSize(2,2)
  console.log('Argumentos recibidos:', args);
  printer.alignCenter();
  printer.println('NUMERO '+type +num);
  printer.println("");

  try {
    // Usar await dentro de una función async
    await printer.printImage('./logo2.png')
    printer.cut();
    
    let execute = printer.execute()
    console.log("Print done!");
  } catch (error) {
    console.error("Print failed:", error);
  }
}

// Llamar a la función async para imprimir el ticket
if ( checkImpresora()) {
  console.log("Se creo correctamente");
  imprimirTicket();
}
else{
  console.log("Error en creacion");
};

