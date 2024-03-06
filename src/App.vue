<template>
  <div class="mianPage">
    <mian />
    <mianInfo />
    <!-- <div class="info">
    </div> -->
    <!-- <vue-draggable-resizable :w="100" :h="100" :parent="false">
      <p>Hello! I'm a flexible component. You can drag me around and you can resize me.</p>
    </vue-draggable-resizable>
    <vue-draggable-resizable :w="100" :h="100" :parent="false">
      <p>Hello! I'm a flexible component. You can drag me around and you can resize me.</p>
    </vue-draggable-resizable>
    <vue-draggable-resizable :w="100" :h="100" :parent="false">
      <p>Hello! I'm a flexible component. You can drag me around and you can resize me.</p>
    </vue-draggable-resizable> -->
  </div>
</template>

<script setup>
import { ref } from "vue";
import mian from "./components/d3/mian.vue";
import mianInfo from "./components/info/mianInfo.vue";
</script>

<style>
@import "vue-draggable-resizable/style.css";
.mianPage {
  padding: 0px;
  margin: 0;
  width: 100vw;
  height: 100vh;
  background-color: white;
  overflow: hidden;
  position: relative;
}

.test {
  position: absolute;
  width: 100px;
  height: 100px;
  background-color: red;
}
.info {
  position: absolute;
  width: 300px;
  height: 100px;
  border: 3px solid black;
  position: absolute;
  top: 50px;
  right: 50px;
}
</style>
