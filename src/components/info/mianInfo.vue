<template>
  <vue-draggable-resizable
    :parent="false"
    class-name="toolbar"
    :w="400"
    :h="900"
  >
    <div class="macos"></div>
    <div class="mianpage"></div>
  </vue-draggable-resizable>
</template>

<style>
.toolbar {
  width: 400px;
  height: 900px;
  border: 3px solid black;
  border-radius: 10px;
  position: absolute;
  top: 50px;
  right: 50px;
  padding: 0px;

}

.macos {
  width: 100%;
  height: 40px;
  background-color: rgba(50, 50, 50, 0.3);
  border-bottom: 3px solid black;
}

.mianpage {
  width: 100%;
  height: calc(100% - 43px);
  background-color: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(5px);
}
</style>
