<template>
  <v-app>
    <v-container>
      <WebSocketComponent />
    </v-container>
  </v-app>
</template>

<script>
import WebSocketComponent from './components/WebSocketComponent.vue';

export default {
  components: {
    WebSocketComponent
  }
};
</script>

<style>
/* Ajoutez vos styles globaux ici */
</style>
