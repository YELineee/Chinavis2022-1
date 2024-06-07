<template>
  <div ref="chartRef" style="width: 370px; height: 370px"></div>
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
    trigger: 'item'
  },
  radar: {
    indicator: [
      { text: 'IP', max: 400 },
      { text: 'Doumain', max: 400 },
      { text: 'Cert', max: 400 },
      { text: 'ASN', max: 400 },
      { text: 'Whois', max: 400 }
    ]
  },
  series: (function () {
    var series = [];
    for (var i = 1; i <= 28; i++) {
      series.push({
        type: 'radar',
        symbol: 'none',
        lineStyle: {
          width: 1
        },
        emphasis: {
          areaStyle: {
            color: 'rgba(0,250,0,0.3)'
          }
        },
        data: [
          {
            value: [
              (40 - i) * 10,
              (38 - i) * 4 + 60,
              i * 5 + 10,
              i * 9,
              (i * i) / 2
            ],
            name: i + 2000 + ''
          }
        ]
      });
    }
    return series;
  })()
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
  setTimeout(() => {
    if (chartRef.value) {
      myChart = echarts.init(chartRef.value);
      myChart.setOption(option);
    }
  }, 10);
  // if (chartRef.value) {
  //   myChart = echarts.init(chartRef.value);
  //   myChart.setOption(option);
  // }
    myChart?.resize();
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
