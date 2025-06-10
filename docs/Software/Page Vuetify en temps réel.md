#benjamin
Dans cette section, on voit comment après avoir mis en place une page web avec Vuetify accessible par exemple par un téléphone sur le même réseau, on peut utiliser les [[WebSocket]]pour afficher en temps réel des informations. Dans cet exemple, on affiche des messages envoyés par le téléphone et l'ordinateur sur la page.
![500](attachments/Pasted%20image%2020250526135537.png)![200](attachments/Pasted%20image%2020250526135812.png)
L'ensemble des fichiers pour ce test peut se retrouver dans le dossier Test WebSocket.
Le programme ne fonctionne probablement pas tel quel : il faut remplacer dans "src/components/WebSocketComponent.vue" à la ligne 35 :
```
this.socket = io("http://147.215.206.226:3000"); 
// Remplacer 147.215.206.226 par son IP (obtenable avec la commande "ifconfig")
```
de même dans server.js ligne 9 :
```
origin: "http://147.215.206.226:8080"
```
Les fichiers contiennent pas mal de lignes inutiles à la compréhension des WebSocket. 
Voilà les instructions clés dans la partie script de WebSocketComponent.vue:
```
<script>
import { io } from "socket.io-client";

export default {
  data() {
    return {
      socket: null,
      message: '',
      messages: []
    };
  },
  mounted() {
    this.socket = io("http://147.215.206.226:3000");
    this.socket.on("message", (msg) => {
      this.messages.push(msg);
    });
  },
  methods: {
    sendMessage() {
      if (this.message) {
        this.socket.emit("message", this.message);
        this.message = '';
      }
    }
  },
  beforeDestroy() {
    if (this.socket) {
      this.socket.disconnect();
    }
  }
};
</script>
```
Dans le fichier server.js : 
```
const express = require("express");
const http = require("http");
const { Server } = require("socket.io");

const app = express();
const server = http.createServer(app);
const io = new Server(server, {
  cors: {
    origin: "http://147.215.206.226:8080",
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

```
Le [[CORS]] est nécessaire puisqu'il y a un serveur qui communique avec la page par des adresses différentes.

