<template>
  <div class="mianContainer">
    <div
      class="toolBox"
      :style="{
        backgroundColor: componentVisibility.mainInfo
          ? 'rgba(255, 255, 255, 0.7)'
          : 'initial',
      }"
      @click="toggleComponent('mainInfo')"
    >
      <svg
        width="40px"
        height="40px"
        viewBox="0 0 24 24"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
        <g
          id="SVGRepo_tracerCarrier"
          stroke-linecap="round"
          stroke-linejoin="round"
        ></g>
        <g id="SVGRepo_iconCarrier">
          <path
            d="M4 18V6"
            stroke="#1C274C"
            stroke-width="1.5"
            stroke-linecap="round"
          ></path>
          <path
            d="M20 6V18"
            stroke="#1C274C"
            stroke-width="1.5"
            stroke-linecap="round"
          ></path>
          <path
            d="M12 10C16.4183 10 20 8.20914 20 6C20 3.79086 16.4183 2 12 2C7.58172 2 4 3.79086 4 6C4 8.20914 7.58172 10 12 10Z"
            stroke="#1C274C"
            stroke-width="1.5"
          ></path>
          <path
            d="M20 12C20 14.2091 16.4183 16 12 16C7.58172 16 4 14.2091 4 12"
            stroke="#1C274C"
            stroke-width="1.5"
          ></path>
          <path
            d="M20 18C20 20.2091 16.4183 22 12 22C7.58172 22 4 20.2091 4 18"
            stroke="#1C274C"
            stroke-width="1.5"
          ></path>
        </g>
      </svg>
    </div>
    <div class="toolBox"></div>
    <div class="toolBox"></div>
    <div class="toolBox"></div>
  </div>
</template>

<script setup>
import { useStatesStore } from "@/stores/states";

const store = useStatesStore();

const { d3States, componentVisibility, toggleComponent } = store;
</script>

<style scoped>
.mianContainer {
  width: auto;
  height: auto;
  padding: 5px;
  border: 3px solid black;
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(50, 50, 50, 0.3);
}

.toolBox {
  width: 70px;
  height: 70px;
  margin: 5px;
  border: 1px solid black;
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
