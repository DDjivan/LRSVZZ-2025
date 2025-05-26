<template>
  <v-container>
    <v-card>
      <v-card-title>WebSocket Demo</v-card-title>
      <v-card-text>
        <v-textarea v-model="message" label="Message" rows="3"></v-textarea>
        <v-btn @click="sendMessage">Envoyer</v-btn>
      </v-card-text>
      <v-card-text>
        <v-list>
          <v-list-item-group>
            <v-list-item v-for="(msg, index) in messages" :key="index">
              <v-list-item-content>{{ msg }}</v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-card-text>
    </v-card>
  </v-container>
</template>

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
    // Remplacez l'URL par celle de votre serveur WebSocket
    this.socket = io("http://147.215.206.226:3000"); // Remplacez par votre adresse IP publique

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

<style scoped>
/* Ajoutez vos styles ici */
</style>
