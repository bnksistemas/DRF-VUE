<template>
  <div class="contaier">
    <!-- Barra de navegación -->
    <navbar-component @productosActualizados="updateProducts" />
    <router-view :products="products" />
    <!-- Usar el componente Footer -->
    <footer-component/>
    
  </div>
</template>
<script setup>
  import { ref } from 'vue';
  // import NavbarComponent from './components/NavbarComponent.vue';

  import NavbarComponent from './components/NavbarComponent.vue';
  import FooterComponent from './components/FooterComponent.vue';

  const products = ref([]);

  function updateProducts(productosBuscados) {
    products.value = productosBuscados;
  }

</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
