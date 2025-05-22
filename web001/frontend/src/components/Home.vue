<template>
  <v-card>
    <v-card-title>Home Page</v-card-title>
    <v-card-text>
      <p>This is a simple home page.</p>
      <v-btn @click="fetchData">Fetch Data from Flask</v-btn>
      <p>{{ message }}</p>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      message: 'message par défaut s',
    };
  },
  methods: {
    async fetchData() {
      const response = await fetch('http://127.0.0.1:5000/api/data'); //adresse du backend flask défini dans app.py
      const data = await response.json(); //réponse du backend sous format json
      this.message = data.message;
    },
  },
};
</script>

<style scoped>
/* Add component-specific styles here */
</style>
