import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue'; 
import Articulos from '../views/Articulos.vue';
import Proveedores from '../views/Proveedores.vue';
import Clientes from '../views/Clientes.vue'; 

const routes = [
  {
    path: '/',
    name: 'Home',
    props: true, // Habilitar props
    component: Home
  },
  {
    path: '/articulos',
    name: 'Articulos',
    component: Articulos
  },
  {
    path: '/proveedores',
    name: 'Proveedores',
    component: Proveedores
  },
  {
    path: '/clientes',
    name: 'Clientes',
    component: Clientes
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router


