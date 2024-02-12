// nodejs_servidor.js
const express = require('express');
const httpProxy = require('http-proxy');
const path = require('path');

// Define los puertos para el servidor Python y el servidor Node.js
const pythonPort = 8000;
const nodePort = 3000;

// Crea un servidor express
const app = express();

// Crea un proxy para redirigir las solicitudes al servidor Python
const proxy = httpProxy.createProxyServer({
  target: `http://127.0.0.1:${pythonPort}`,
  // o también puedes usar target: `http://localhost:${pythonPort}`,
});

// Middleware para manejar las solicitudes estáticas
app.use('/calculadora', express.static(path.join(__dirname, 'calculadora')));

// Redirige todas las demás solicitudes al servidor Python
app.all('*', (req, res) => {
  proxy.web(req, res);
});

// Imprime la información del servidor Node.js
app.listen(nodePort, () => {
  console.log(`Servidor Node.js ejecutándose en http://localhost:${nodePort}/`);
});
