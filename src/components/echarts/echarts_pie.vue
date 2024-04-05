<template>
   <div ref="chartRef" style="width: 100%; height: 500px"></div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from "vue";
import * as echarts from "echarts";

const chartRef = ref<HTMLElement | null>(null);

const option = {
   tooltip: {
      trigger: "item",
   },
   legend: {
      orient: "vertical",
      left: "left",
   },
   series: [
      {
         name: "Access From",
         type: "pie",
         radius: "50%",
         data: [
            { value: 1048, name: "Search Engine" },
            { value: 735, name: "Direct" },
            { value: 580, name: "Email" },
            { value: 484, name: "Union Ads" },
            { value: 300, name: "Video Ads" },
         ],
         emphasis: {
            itemStyle: {
               shadowBlur: 10,
               shadowOffsetX: 0,
               shadowColor: "rgba(0, 0, 0, 0.5)",
            },
         },
      },
   ],
};

let myChart: echarts.ECharts | null = null;

onMounted(() => {
   if (chartRef.value) {
      myChart = echarts.init(chartRef.value);
      myChart.setOption(option);
   }
});

onBeforeUnmount(() => {
   if (myChart) {
      myChart.dispose();
      myChart = null;
   }
});

import { defineExpose } from "vue";

defineExpose({
   resizeChart() {
      if (myChart) {
         myChart.resize();
      }
   },
});
</script>
