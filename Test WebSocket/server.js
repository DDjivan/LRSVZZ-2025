const express = require("express");
const http = require("http");
const { Server } = require("socket.io");

const app = express();
const server = http.createServer(app);
const io = new Server(server, {
  cors: {
    origin: "http://192.168.218.54:8080", // Remplacez par l'URL de votre application Vue.js
    methods: ["GET", "POST"],
    allowedHeaders: ["my-custom-header"],
    credentials: true
  }
});

io.on("connection", (socket) => {
  console.log("Un utilisateur est connecté");

  socket.on("message", (msg) => {
    console.log("Message reçu: " + msg);
    io.emit("message", msg); // Émet le message à tous les clients
  });

  socket.on("disconnect", () => {
    console.log("Un utilisateur est déconnecté");
  });
});

server.listen(3000, () => {
  console.log("Serveur WebSocket en écoute sur le port 3000");
});
