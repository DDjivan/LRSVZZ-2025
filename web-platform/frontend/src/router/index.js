import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/Home.vue'; // Ensure you have this component
import About from '../components/About.vue'; // Create this component

const routes = [
  { path: '/', name: 'Home', component: Home },
{ path: '/about', name: 'About', component: About },
];

const router = createRouter({
  history: createWebHistory(),
                            routes,
});

export default router;
