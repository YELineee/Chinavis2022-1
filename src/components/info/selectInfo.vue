<template>
  <vue-draggable-resizable
    class-name="toolbar"
    :w="400"
    :h="800"
    :min-width="400"
    :min-height="800"
    :drag-handle="'.macos'"
    :resizable="true"
    ref="toolbarRef"
  >
    <div class="macos" ref="macosRef">
      <div class="xButton" @click="hideComponent('selectInfo')">
        <svg
          width="30px"
          height="30px"
          viewBox="0 -0.5 25 25"
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
              d="M6.96967 16.4697C6.67678 16.7626 6.67678 17.2374 6.96967 17.5303C7.26256 17.8232 7.73744 17.8232 8.03033 17.5303L6.96967 16.4697ZM13.0303 12.5303C13.3232 12.2374 13.3232 11.7626 13.0303 11.4697C12.7374 11.1768 12.2626 11.1768 11.9697 11.4697L13.0303 12.5303ZM11.9697 11.4697C11.6768 11.7626 11.6768 12.2374 11.9697 12.5303C12.2626 12.8232 12.7374 12.8232 13.0303 12.5303L11.9697 11.4697ZM18.0303 7.53033C18.3232 7.23744 18.3232 6.76256 18.0303 6.46967C17.7374 6.17678 17.2626 6.17678 16.9697 6.46967L18.0303 7.53033ZM13.0303 11.4697C12.7374 11.1768 12.2626 11.1768 11.9697 11.4697C11.6768 11.7626 11.6768 12.2374 11.9697 12.5303L13.0303 11.4697ZM16.9697 17.5303C17.2626 17.8232 17.7374 17.8232 18.0303 17.5303C18.3232 17.2374 18.3232 16.7626 18.0303 16.4697L16.9697 17.5303ZM11.9697 12.5303C12.2626 12.8232 12.7374 12.8232 13.0303 12.5303C13.3232 12.2374 13.3232 11.7626 13.0303 11.4697L11.9697 12.5303ZM8.03033 6.46967C7.73744 6.17678 7.26256 6.17678 6.96967 6.46967C6.67678 6.76256 6.67678 7.23744 6.96967 7.53033L8.03033 6.46967ZM8.03033 17.5303L13.0303 12.5303L11.9697 11.4697L6.96967 16.4697L8.03033 17.5303ZM13.0303 12.5303L18.0303 7.53033L16.9697 6.46967L11.9697 11.4697L13.0303 12.5303ZM11.9697 12.5303L16.9697 17.5303L18.0303 16.4697L13.0303 11.4697L11.9697 12.5303ZM13.0303 11.4697L8.03033 6.46967L6.96967 7.53033L11.9697 12.5303L13.0303 11.4697Z"
              fill="#000000"
            ></path>
          </g>
        </svg>
      </div>
    </div>
    <div class="mainpage" ref="mainpageRef">
      <div class="mainInfo">
        <div class="inputBox">
          <div>起点<input type="text" /></div>
          <div>-----></div>
          <div>终点<input type="text" /></div>
        </div>
        <div class="allNode">
          <div class="nodeTitle">
            <div>途径节点:</div>
            <div class="search">
              <svg
                width="30px"
                height="30px"
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
                    d="M15.7955 15.8111L21 21M18 10.5C18 14.6421 14.6421 18 10.5 18C6.35786 18 3 14.6421 3 10.5C3 6.35786 6.35786 3 10.5 3C14.6421 3 18 6.35786 18 10.5Z"
                    stroke="#000000"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  ></path>
                </g>
              </svg>
            </div>
          </div>
          <div class="nodeList">
            <div class="node" v-for="(node, index) in nodes" :key="index">
              <input type="checkbox" class="checkbox" v-model="node.checked" />
              <div class="nodeName">{{ node.name }}</div>
              <div>
                <svg
                  width="30px"
                  height="30px"
                  viewBox="0 0 24 24"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                  transform="matrix(1, 0, 0, 1, 0, 0)"
                >
                  <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                  <g
                    id="SVGRepo_tracerCarrier"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke="#CCCCCC"
                    stroke-width="0.4800000000000001"
                  ></g>
                  <g id="SVGRepo_iconCarrier">
                    <path
                      d="M10 12L14 16M14 12L10 16M4 6H20M16 6L15.7294 5.18807C15.4671 4.40125 15.3359 4.00784 15.0927 3.71698C14.8779 3.46013 14.6021 3.26132 14.2905 3.13878C13.9376 3 13.523 3 12.6936 3H11.3064C10.477 3 10.0624 3 9.70951 3.13878C9.39792 3.26132 9.12208 3.46013 8.90729 3.71698C8.66405 4.00784 8.53292 4.40125 8.27064 5.18807L8 6M18 6V16.2C18 17.8802 18 18.7202 17.673 19.362C17.3854 19.9265 16.9265 20.3854 16.362 20.673C15.7202 21 14.8802 21 13.2 21H10.8C9.11984 21 8.27976 21 7.63803 20.673C7.07354 20.3854 6.6146 19.9265 6.32698 19.362C6 18.7202 6 17.8802 6 16.2V6"
                      stroke="#000000"
                      stroke-width="2"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    ></path>
                  </g>
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </vue-draggable-resizable>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useStatesStore } from "@/stores/states";

import echarts_pie from "../echarts/echarts_pie.vue";
import axios from "axios";

const store = useStatesStore();
const { hideComponent } = store;

const macosRef = ref<HTMLElement | null>(null);

const nodes = [
  { name: "Domain_a2d2208c5348b93e3ddc90439ae6c7eda49cde8...", checked: false },
  { name: "Domain_a2d2208c5348b93e3ddc90439ae6c7eda49cde8...", checked: false },
  { name: "Domain_a2d2208c5348b93e3ddc90439ae6c7eda49cde8...", checked: false },
  { name: "Domain_a2d2208c5348b93e3ddc90439ae6c7eda49cde8...", checked: false },
  { name: "Domain_a2d2208c5348b93e3ddc90439ae6c7eda49cde8...", checked: false },
  { name: "Domain_e5e34ad079fa8e284b47409407dde50949da066...", checked: false },
  { name: "IP_86d674eeb343174e4539a238082511242e11acee691...", checked: false },
  { name: "IP_86d674eeb343174e4539a238082511242e11acee691...", checked: false },
  { name: "Domain_e5e34ad079fa8e284b47409407dde50949da066...", checked: false },
  { name: "Domain_e5e34ad079fa8e284b47409407dde50949da066...", checked: false },
  { name: "Domain_a862079db9fcb59b2b81b3a114aced6a857fd0a...", checked: false },
  { name: "Domain_5908b907c4faf7a2bbf7e2b9a25b29c52f08572...", checked: false },
  // 更多节点...
];
</script>

<style scoped>
.toolbar {
  width: 400px;
  height: 700px;
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
  min-height: 40px;
  background-color: rgba(50, 50, 50, 0.3);
  border-bottom: 3px solid black;
}

.mainpage {
  background-color: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(5px);
  flex: 1;
  padding: 10px;
}

:deep(h2) {
  margin: 0;
}

:deep(h4) {
  margin: 5px 0 5px 0;
}

.xButton {
  position: absolute;
  right: 3;
  top: 2;
  cursor: pointer;
  padding: 5px;
}

.mainInfo {
  padding: 15px;
}

input {
  width: 50px;
  height: 30px;
  margin-left: 5px;
  background-color: rgba(0, 0, 0, 0.155);
  border-radius: 2px;
  border: 2px solid black;
}
.nodeTitle,
.inputBox {
  display: flex;
  justify-content: space-between;
}

.nodeTitle {
  margin-top: 20px;
  margin-bottom: 10px;
}
.node {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 10px;
}
.checkbox {
  width: 20px;
  height: 20px;
}
.nodeName {
  margin-inline: 10px;
  font-size: 16px;
  overflow: hidden;
}
.search {
  margin-right: 10px;
}
</style>
