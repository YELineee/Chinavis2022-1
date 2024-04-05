<template>
  <vue-draggable-resizable
    class-name="toolbar"
    :w="400"
    :min-width="400"
    :h="'auto'"
    :min-height="700"
    :drag-handle="'.macos'"
    :resizable="true"
  >
    <div class="macos" @dblclick="handleDbClick()"></div>
    <div class="mainpage">
      <div class="mainInfo">
        <h2>Main Information</h2>
        <h4>Node count: {{ typeCount }}</h4>
        <h4>Link count:</h4>
        <h4>Type count:</h4>
        <echarts_pie ref="chartRef" />
      </div>
    </div>
    <div class="reSizeButton">

    </div>
  </vue-draggable-resizable>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import echarts_pie from '../echarts/echarts_pie.vue';
const typeCount = ref("11");

const handleDbClick = () => {
 
};
</script>



<style scoped>
.toolbar {
  width: 400px;
  height: 100%;
  border: 3px solid black;
  border-radius: 10px;
  top: 50px;
  right: 50px;
  padding: 0px;
  display: flex; 
  flex-direction: column; 
  /* position: absolute; */
}

.macos {
  width: 100%;
  height: 40px;
  background-color: rgba(50, 50, 50, 0.3);
  border-bottom: 3px solid black;
}

.mainpage {
  background-color: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(5px);
  flex: 1;
  padding: 10px;
}

.reSizeButton{
  width: 40px;
  height: 40px;
  background-color: rgba(50, 50, 50, 0.3);
  position: absolute;
  bottom: 0;
  right: 0;
}

:deep(h2) {
  margin: 0;  
}

:deep(h4) {
  margin: 5px 0 5px 0;  
}
</style>