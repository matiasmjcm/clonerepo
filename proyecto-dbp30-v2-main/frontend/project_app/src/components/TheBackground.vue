<template>
  <div id="mainBackground"></div>
</template>

<script>
export default {
  name: "TheBackground",
};
</script>

<style scoped>
#mainBackground {
  width: 100%;
  height: 100vh;
  background-image: linear-gradient(rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.75)),
    url("../assets/libreria_fondo.jpg");
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
}
</style>
