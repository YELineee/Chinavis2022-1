<template>
  <div ref="chartRef" style="width: 900px; height: 400px"></div>
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
  series: {
    type: "sankey",
    layout: "none",
    emphasis: {
      focus: "adjacency",
    },
    data: [
      {
        name: "a",
      },
      {
        name: "b",
      },
      {
        name: "a1",
      },
      {
        name: "a2",
      },
      {
        name: "b1",
      },
      {
        name: "c",
      },
    ],
    links: [
      {
        source: "a",
        target: "a1",
        value: 5,
      },
      {
        source: "a",
        target: "a2",
        value: 3,
      },
      {
        source: "b",
        target: "b1",
        value: 8,
      },
      {
        source: "a",
        target: "b1",
        value: 3,
      },
      {
        source: "b1",
        target: "a1",
        value: 1,
      },
      {
        source: "b1",
        target: "c",
        value: 2,
      },
    ],
  },
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
