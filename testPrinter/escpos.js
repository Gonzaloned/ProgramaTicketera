// main.js

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function requestSerialAccess() {
    try {
        const port = await navigator.serial.requestPort();
        // Configura el flujo de lectura/escritura y otros ajustes necesarios aquí
        // ...
        return port;
    } catch (err) {
        console.error('Error al solicitar acceso al puerto serie:', err);
        return null;
    }
}

async function sendCommandToPrinter(port, command) {
    try {
        if (!port) throw new Error('El puerto serie no está disponible.');

        const writer = port.writable.getWriter();
        await writer.write(command);
        await writer.releaseLock();
    } catch (err) {
        console.error('Error al enviar comando a la impresora:', err);
    }
}

async function init() {
    await sleep(100); // Esperar un corto período de tiempo para obtener permisos

    // Comando ESC/POS para imprimir texto
    const textToPrint = '¡Hola, mundo!\nEsta es una impresión de prueba desde JavaScript.\n\n\n\n';
    const command = new TextEncoder().encode(textToPrint);

    try {
        const printerPort = await requestSerialAccess();
        await sendCommandToPrinter(printerPort, command);
    } catch (err) {
        console.error('Error durante la impresión:', err);
    }
}

init();
