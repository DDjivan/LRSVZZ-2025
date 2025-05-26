import { createApp } from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify'; // Import Vuetify plugin
import { createRouter, createWebHistory } from 'vue-router'; // Optional: For routing

// Create a simple router (optional)
const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('./components/Home.vue'), // Lazy load Home component
  },
];

const router = createRouter({
  history: createWebHistory(),
                            routes,
});

const app = createApp(App);
app.use(vuetify); // Use Vuetify
app.use(router); // Use router if you set it up
app.mount('#app');
