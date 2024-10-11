<template>
    <!-- Carrusel de imágenes -->
    <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel" data-bs-interval="2000">
    <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="3" aria-label="Slide 4"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="4" aria-label="Slide 5"></button>
    </div>
    <div class="carousel-inner">
        <div class="carousel-item active">
            <img :src="require('@/assets/images/2.jpg')" class="img-fluid" alt="Imagen1" style="height: 400px;">
        </div>
        <div class="carousel-item">
            <img :src="require('@/assets/images/3.jpg')" class="img-fluid" alt="Imagen2" style="height: 400px;">
        </div>
        <div class="carousel-item">
            <img :src="require('@/assets/images/4.jpg')" class="img-fluid" alt="Imagen3" style="height: 400px;">
        </div>
        <div class="carousel-item">
            <img :src="require('@/assets/images/5.jpg')" class="img-fluid" alt="Imagen4" style="height: 400px;">
        </div>
        <div class="carousel-item">
            <img :src="require('@/assets/logo.png')" class="img-fluid" alt="Imagen4" style="height: 400px;">
        </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Anterior</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Siguiente</span>
    </button>
    </div>
</template>

<script setup>

</script>

<style scoped>
</style>