<template>
  <div>
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
  </div>
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
  { name: "Domain_a2d2208c5348439ae8...", checked: false },
  { name: "Domain_a2d2208c5348439ae8...", checked: false },
  { name: "Domain_a2d2208c5348439ae8...", checked: false },
  { name: "Domain_a2d2208c5348439ae8...", checked: false },
  { name: "Domain_a2d2208c5348439ae8...", checked: false },
  { name: "Domain_e5e34ad0750949d066...", checked: false },
  { name: "IP_86d674eeb3432e11aa23ce691...", checked: false },
  { name: "IP_86d674ee11242e11ee36691...", checked: false },
  { name: "Domain_e5e34ad3fsa3949da66...", checked: false },
  { name: "Domain_e5e34ad4ad00949da06...", checked: false },
  // { name: "Domain_a862079db9fcb59b2b81b3a114aced6a857fd0a...", checked: false },
  // { name: "Domain_5908b907c4faf7a2bbf7e2b9a25b29c52f08572...", checked: false },
  // 更多节点...
];
</script>

<style scoped>
.toolbar {
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

.mainpage {
  background-color: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(5px);
  flex: 1;
  padding: 10px;
  border: 3px solid black;
  border-radius: 10px;
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
  max-width: 250px;
}
.search {
  margin-right: 10px;
}
</style>
