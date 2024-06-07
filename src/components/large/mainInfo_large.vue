<template>
   <div>
     <div class="mainpage" ref="mainpageRef">
       <div class="mainInfo">
         
         <h4 @click="updateData()">Node count: {{ nodesCount }}</h4>
         <h4>Link count: {{ linksCount }}</h4>
         <echarts_pie
           ref="chartRef"
           v-if="getData"
           :pieData="pieData"
           :linksCount="linksCount"
         />
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
 
 const getData = ref(false);
 
 const nodesCount = ref<number>();
 const linksCount = ref<number>();
 const pieData = ref<object>();
 
 const chartRef = ref<HTMLElement | null>(null);
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
   width: full;
   height: full;
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
   background-color: rgba(255, 255, 255,0.9);
   backdrop-filter: blur(5px);
   flex: 1;
   padding: 10px;
   border: 3px solid black;
   border-radius: 10px;
   width: full;
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
 