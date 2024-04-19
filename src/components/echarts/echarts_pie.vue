<template>
  <div ref="chartRef" style="width: 100%; height: 550px"></div>
</template>

<script setup lang="ts">
import {
  ref,
  onMounted,
  onBeforeUnmount,
  defineExpose,
  defineProps,
  watch,
} from "vue";
import * as echarts from "echarts";

let myChart: echarts.ECharts | null = null;

const chartRef = ref<HTMLElement | null>(null);

const props = defineProps({
  pieData: Object,
});

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
      data: props.pieData,
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

watch(
  () => props.pieData,
  () => {
    if (myChart) {
      myChart.setOption({
        series: [
          {
            data: props.pieData,
          },
        ],
      });
    }
  },
);

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

defineExpose({
  resizeChart() {
    if (myChart) {
      myChart.resize();
    }
  },
});
</script>
