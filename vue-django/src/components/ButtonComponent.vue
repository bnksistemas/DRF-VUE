<template>
    <!-- Botones de categorías -->
    <div class="text-center mt-4 mb-4">
        <div class="row justify-content-center g-1 g-md-1">
            <div class="col-12 col-md-auto mb-1 mb-md-3" v-for="nombre in nombres" :key="nombre.id">
                <!--Cuando se hace clic en un botón, llama al método filterBySupplier -->
                <button
                    type="button" 
                    class="btn btn-secondary w-100"
                    @click="filterBySupplier(nombre.id, nombre.name)"> <!-- Detectamos el clic en el boton -->
                    {{ nombre.name.trim() }}
                </button>
            </div>
        </div>
    </div>

    <hr>
</template>
<script setup>
// 1) importo axios y declaro variables reactivas
import axios from 'axios'
import { ref, onMounted } from 'vue'

// 2) Variables reactivas
const nombres = ref([])
// Emisión del evento para el componente padre
const emit = defineEmits(['supplierSelected']);


// 3) Llamada API cuando el componente se monta
onMounted(() => {
    axios.get('http://127.0.0.1:8000/api/supplier/')
        .then(response => {
        nombres.value = response.data
    })
    .catch(error => {
        console.log(error)
    });
})

// 4) Función que emite el evento al hacer clic en un botón

function filterBySupplier(supplierId, supplierName) {
    // Emitimos un evento personalizado 'supplierSelected' con el id y nombre del proveedor seleccionado
    // Con 'emit' se maneja en script setup
    emit('supplierSelected', supplierId, supplierName);
}

</script>

<style scoped>

</style>