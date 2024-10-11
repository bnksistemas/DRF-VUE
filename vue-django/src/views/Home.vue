<template>

<!-- <navbar-component  @productosActualizados="updateProducts" v-if="$route.path !='/'"></navbar-component> -->
<CarruselComponent></CarruselComponent>
<button-component @supplierSelected="getProductsBySupplier"></button-component>




<!-- Botón para mostrar todos los productos -->
<div v-if="selectedSupplierName">
    <button @click="getAllProducts" class="btn btn-primary my-3">
        Mostrar todos los productos
    </button>
</div>
<section>
    <!-- Mostrar el mensaje basado en si hay productos o no -->
    <div v-if="selectedSupplierName">
        <h5 v-if="products.length > 0">
            Artículos del proveedor: <strong>{{ selectedSupplierName }}</strong>
        </h5>
        <h5 v-else class="no-products-message">
            No hay productos cargados aún para el proveedor <strong>{{ selectedSupplierName }}</strong>
        </h5>
    </div>
    
    <!-- Sección de productos -->
    <div class="row row-cols-1 row-cols-md-3 g-4">
        <div class="col" v-for="product in products" :key="product.id">
            <div class="card text-center">
                <img :src="product.image" class="card-img-top" alt="Imagen de {{ product.name }}">
                <div class="card-body">
                    <h5 class="card-title">{{product.code}} - {{product.name }}</h5>
                    <h6 class="card-subtitle mb-2 text-body-secondary">{{ product.supplier_name }}</h6>
                    <p class="card-text">{{product.description}}</p>
                    <p class="card-text">Color: {{product.color_choice_description}}</p>
                </div>
                <div class="card-footer text-danger">
                    $ {{ product.price }}
                </div>
            </div>
        </div>
    </div>
</section>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { defineProps } from 'vue';
// import NavbarComponent from '@/components/NavbarComponent.vue';
import CarruselComponent from "@/components/CarruselComponent.vue";
import ButtonComponent from "@/components/ButtonComponent.vue";
import axios from 'axios';

const products = ref([]);
const selectedSupplierName = ref('');

const props = defineProps({
    products: {
    type: Array,
    default: () => [],
    
    },  
});
console.log('Products:', props.products); // Verifica el contenido de products

// Obtener todos los productos
function getProducts() {
    axios.get('http://127.0.0.1:8000/api/product/').then((response) =>{
        products.value = response.data
    })
}
function getAllProducts() {
    axios.get('http://127.0.0.1:8000/api/product/').then((response) => {
        products.value = response.data;
        selectedSupplierName.value = '';
    }).catch((error) => {
        console.error('Error al obtener todos los productos:', error);
    });
}

// Obtener productos por proveedor
function getProductsBySupplier(supplierId, supplierName) {
    axios.get(`http://127.0.0.1:8000/api/product/?supplier=${supplierId}`)
        .then((response) => {
        products.value = response.data;
        selectedSupplierName.value = supplierName;
    })
    .catch((error) => {
        console.error('Error al obtener productos:', error);
    });
}
/* // Actualizar productos desde la búsqueda
function updateProducts(productosBuscados) {
    products.value = productosBuscados;
    selectedSupplierName.value = '';
}
 */
// Llamar a getProducts al cargar el componente
onMounted(() => {
    getProducts();
});


</script>

<style>
    .card {
        border: 2px solid gray !important;
    }
    .no-products-message {
        margin-top: 20px;
        text-align: center;
        color: rgb(216, 100, 23); /* Ajusta el color o estilo según prefieras */
    }
    footer {
        margin-top: 20px;
    }
</style>