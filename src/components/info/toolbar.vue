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
    <div
      class="toolBox"
      :style="{
        backgroundColor: componentVisibility.chartsInfo
          ? 'rgba(255, 255, 255, 0.7)'
          : 'initial',
      }"
      @click="toggleComponent('chartsInfo')"
    >
      <svg fill="#000000" width="40px" height="40px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M29.5 7c-1.381 0-2.5 1.12-2.5 2.5 0 0.284 0.058 0.551 0.144 0.805l-6.094 5.247c-0.427-0.341-0.961-0.553-1.55-0.553-0.68 0-1.294 0.273-1.744 0.713l-4.774-2.39c-0.093-1.296-1.162-2.323-2.482-2.323-1.38 0-2.5 1.12-2.5 2.5 0 0.378 0.090 0.732 0.24 1.053l-4.867 5.612c-0.273-0.102-0.564-0.166-0.873-0.166-1.381 0-2.5 1.119-2.5 2.5s1.119 2.5 2.5 2.5c1.381 0 2.5-1.119 2.5-2.5 0-0.332-0.068-0.649-0.186-0.939l4.946-5.685c0.236 0.073 0.48 0.124 0.74 0.124 0.727 0 1.377-0.316 1.834-0.813l4.669 2.341c0.017 1.367 1.127 2.471 2.497 2.471 1.381 0 2.5-1.119 2.5-2.5 0-0.044-0.011-0.086-0.013-0.13l6.503-5.587c0.309 0.137 0.649 0.216 1.010 0.216 1.381 0 2.5-1.119 2.5-2.5s-1.119-2.5-2.5-2.5z"></path> </g></svg>
    </div>
    <div
      class="toolBox"
      :style="{
        backgroundColor: componentVisibility.selectInfo
          ? 'rgba(255, 255, 255, 0.7)'
          : 'initial',
      }"
      @click="toggleComponent('selectInfo')"
    >
    <svg width="40px" height="40px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path fill-rule="evenodd" clip-rule="evenodd" d="M5 6C5.55228 6 6 5.55228 6 5C6 4.44772 5.55228 4 5 4C4.44772 4 4 4.44772 4 5C4 5.55228 4.44772 6 5 6ZM18 13C18 12.4477 17.5523 12 17 12C16.4477 12 16 12.4477 16 13V16H13C12.4477 16 12 16.4477 12 17C12 17.5523 12.4477 18 13 18H16V21C16 21.5523 16.4477 22 17 22C17.5523 22 18 21.5523 18 21V18H21C21.5523 18 22 17.5523 22 17C22 16.4477 21.5523 16 21 16H18V13ZM10 5C10 5.55228 9.55228 6 9 6C8.44771 6 8 5.55228 8 5C8 4.44772 8.44771 4 9 4C9.55228 4 10 4.44772 10 5ZM13 6C13.5523 6 14 5.55228 14 5C14 4.44772 13.5523 4 13 4C12.4477 4 12 4.44772 12 5C12 5.55228 12.4477 6 13 6ZM18 5C18 5.55228 17.5523 6 17 6C16.4477 6 16 5.55228 16 5C16 4.44772 16.4477 4 17 4C17.5523 4 18 4.44772 18 5ZM17 10C17.5523 10 18 9.55228 18 9C18 8.44771 17.5523 8 17 8C16.4477 8 16 8.44771 16 9C16 9.55228 16.4477 10 17 10ZM10 17C10 17.5523 9.55228 18 9 18C8.44771 18 8 17.5523 8 17C8 16.4477 8.44771 16 9 16C9.55228 16 10 16.4477 10 17ZM5 18C5.55228 18 6 17.5523 6 17C6 16.4477 5.55228 16 5 16C4.44772 16 4 16.4477 4 17C4 17.5523 4.44772 18 5 18ZM6 13C6 13.5523 5.55228 14 5 14C4.44772 14 4 13.5523 4 13C4 12.4477 4.44772 12 5 12C5.55228 12 6 12.4477 6 13ZM5 10C5.55228 10 6 9.55228 6 9C6 8.44771 5.55228 8 5 8C4.44772 8 4 8.44771 4 9C4 9.55228 4.44772 10 5 10Z" fill="#000000"></path> </g></svg>
  </div>
    <div class="toolBox">
      <svg width="40px" height="40px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M17 17H17.01M17.4 14H18C18.9319 14 19.3978 14 19.7654 14.1522C20.2554 14.3552 20.6448 14.7446 20.8478 15.2346C21 15.6022 21 16.0681 21 17C21 17.9319 21 18.3978 20.8478 18.7654C20.6448 19.2554 20.2554 19.6448 19.7654 19.8478C19.3978 20 18.9319 20 18 20H6C5.06812 20 4.60218 20 4.23463 19.8478C3.74458 19.6448 3.35523 19.2554 3.15224 18.7654C3 18.3978 3 17.9319 3 17C3 16.0681 3 15.6022 3.15224 15.2346C3.35523 14.7446 3.74458 14.3552 4.23463 14.1522C4.60218 14 5.06812 14 6 14H6.6M12 15V4M12 15L9 12M12 15L15 12" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>
    </div>
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
