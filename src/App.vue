<template>
  <div class="mianPage">
    <div class="title" id="title"></div>
    <div class="toolbar">
      <toolBar />
    </div>
    <mian />
    <div class="initBox">
      <mianInfo v-if="componentVisibility.mainInfo" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useStatesStore } from "./stores/states";

import mian from "./components/d3/mian.vue";
import mianInfo from "./components/info/mianInfo.vue";
import toolBar from "./components/info/toolbar.vue";

import TypeIt from "typeit";

const store = useStatesStore();

const { componentVisibility, showComponent, hideComponent } = store;

onMounted(() => {
  createTypeItEffect("#title");
  console.log(componentVisibility);
});

function createTypeItEffect(element, options = {}) {
  // 默认选项
  const defaultOptions = {
    speed: 150,
    loop: true,
    lifeLike: true,
  };

  // 合并用户提供的选项和默认选项
  const mergedOptions = { ...defaultOptions, ...options };

  return new TypeIt(element, mergedOptions)
    .delete()
    .type("Draggable", { delay: 100 })
    .pause(500)
    .move(-4)
    .delete()
    .type("Resize", { delay: 100 })
    .move(4)
    .pause(5000)
    .delete()
    .type("Visualization", { delay: 100 })
    .pause(20000)
    .go();
}
</script>

<style>
@import "vue-draggable-resizable/style.css";

#title {
  font-size: 3em;
  font-weight: bold;
  color: #000;
  position: absolute;
  top: 2%;
  left: 3%;
  font-family: DancingScript;
}

.mianPage {
  padding: 0px;
  margin: 0;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  position: relative;
  font-size: 24px;
  background-color: #ffffff;
}

.initBox {
  width: 0px;
  height: 0px;
  position: absolute;
  top: 5%;
  right: 0;
}
.toolbar {
  border: red 1px solid;
  position: absolute;
  right: 13px;
  bottom: 13px;
}
</style>
