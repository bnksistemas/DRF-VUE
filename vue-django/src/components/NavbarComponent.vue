<template>
    <!-- Nav bar -->
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">
                <img src="logo.png" alt="Calzados Caramelito" width="100" height="50">
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <router-link to="/" class="nav-link active" aria-current="page">Inicio</router-link>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Comercio
                        </a>
                    <ul class="dropdown-menu">
                        <li>
                            <router-link to="/articulos" class="dropdown-item">Artículos</router-link>
                        </li>
                        <li>
                            <router-link to="/proveedores" class="dropdown-item">Proveedores</router-link>
                        </li>
                        <li><hr class="dropdown-divider"></li>
                        <li>
                            <router-link to="/clientes" class="dropdown-item">Clientes</router-link>
                        </li>
                    </ul>
                    </li>
                <li class="nav-item">
                    <router-link class="nav-link" to="/about">Acerca de Nosotros</router-link>
                </li>  
                </ul>
                <form @submit.prevent="searchProducts" class="d-flex" role="search">
                    <input v-model="searchQuery" class="form-control me-2" type="search" placeholder="Buscar" aria-label="Search">
                    <button class="btn btn-outline-success" type="submit">Search</button>
                </form>
            </div>
        </div>
    </nav>
</template>
<script setup>
import { ref, defineEmits } from 'vue';

const searchQuery = ref(''); // Almacenar término de búsqueda
const emit = defineEmits(['productosActualizados']);  // Definir el evento emitido

// Función para manejar la búsqueda
function searchProducts() {
    if (!searchQuery.value) {
        console.warn('Consulta de búsqueda vacía.');
        return;
    }
    fetch(`http://127.0.0.1:8000/api/products/search/?search=${searchQuery.value}`)
    .then((response) => response.json())
    .then((data) => {
      emit('productosActualizados', data); // Emitir los resultados
    })
    .catch((error) => {
        console.error('Error en la búsqueda:', error);
    });
}

</script>

<style scoped>

</style>