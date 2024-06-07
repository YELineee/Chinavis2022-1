<template>
  <div ref="chartRef" style="width: 350px; height: 370px"></div>
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
  legend: {
    top: '5%',
    left: 'center'
  },
  series: [
    {
      name: 'Access From',
      type: 'pie',
      radius: ['40%', '70%'],
      avoidLabelOverlap: false,
      label: {
        show: false,
        position: 'center'
      },
      emphasis: {
        label: {
          show: true,
          fontSize: 40,
          fontWeight: 'bold'
        }
      },
      labelLine: {
        show: false
      },
      data: [
      {
         "name": "Domain",
         "value": 40
      },
      {
         "name": "IP",
         "value": 2
      },
      {
         "name": "Whois_Email",
         "value": 9
      },
      {
         "name": "Whois_Phone",
         "value": 9
      },
      {
         "name": "Whois_Name",
         "value": 6
      },
      {
         "name": "Cert",
         "value": 5
      },
      {
         "name": "IP_C",
         "value": 1
      },
      {
         "name": "ASN",
         "value": 1
      }
      ]
    }
  ]
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
