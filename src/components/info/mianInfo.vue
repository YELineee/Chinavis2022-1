<template>
  <vue-draggable-resizable
    class-name="toolbar"
    :w="400"
    :h="800"
    :drag-handle="'.macos'"
    :resizable="true"
    @resizing="resize"
    ref="toolbarRef"
  >
    <div class="macos" ref="macosRef" @dblclick="handleDbClick()">
      <div class="xButton" @click="hideComponent('mainInfo')">
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
        <h2 @click="updateData()">Main Information</h2>
        <h4>Node count: {{ nodesCount }}</h4>
        <h4>Link count: {{ linksCount }}</h4>
        <h4>Type count:</h4>
        <echarts_pie
          ref="chartRef"
          v-if="getData"
          :pieData="pieData"
          :linksCount="linksCount"
        />
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

const getData = ref(false);

const nodesCount = ref<number>();
const linksCount = ref<number>();
const pieData = ref<object>();

const chartRef = ref<HTMLElement | null>(null);
const macosRef = ref<HTMLElement | null>(null);
const mainpageRef = ref<HTMLElement | null>(null);
const toolbarRef = ref<HTMLElement | null>(null);

const resize = () => {
  (chartRef.value as any).resizeChart();
};

const dispose = () => {
  (chartRef.value as any).disposeChart();
};

// const closePages = () => {
//   (toolbarRef.value as any).$el.style.display = 'none';
// };

const updateData = async () => {
  try {
    const idList = ["CAG1", "CAG2", "CAG3", "CAG4", "CAG5"];
    const id = idList[Math.floor(Math.random() * idList.length)];
    const response = await axios.get(
      `http://127.0.0.1:8000/data/mianInfo?id=${id}`,
    );
    const newData = response.data;

    nodesCount.value = newData.nodesCounts;
    linksCount.value = newData.linksCounts;
    pieData.value = newData.nodesTypeCounts;
  } catch (error) {
    console.error("Error while updating data:", error);
  }
};

const handleDbClick: () => void = () => {
  console.log("dbclick");
  console.log(toolbarRef);
};

onMounted(async () => {
  await axios.get("http://127.0.0.1:8000/data/mianInfo?id=CAG1").then((res) => {
    nodesCount.value = res.data.nodesCounts;
    linksCount.value = res.data.linksCounts;
    pieData.value = res.data.nodesTypeCounts;
    // console.log(pieData);
    getData.value = true;
  });
});
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
</style>
