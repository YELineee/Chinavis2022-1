<template>
   <div class="mainPage">
      <div class="row firstRow">
         <div class="container ">
            <mianInfo_large/>
         </div>
         <div class="container">
            <mian/>
         </div>
         <div class="container">
            <selectInfo/>
         </div>
      </div>
      <div class="row secondRow">
         <div class="container">
            <div class="macos">
               <echarts_nodePie />
            </div>
         </div>
         <div class="container">
            <div class="macos">
               <echarts_sankey />
            </div>
         </div>
      </div>
   </div>
</template>

<script setup>
import mian from '@/components/d3/mian_large.vue';
import mianInfo_large from '@/components/large/mainInfo_large.vue';
import selectInfo from '@/components/large/selectInfo_large.vue';
import echarts_nodePie from '@/components/echarts/echarts_nodePie.vue';
import echarts_sankey from '@/components/echarts/echarts_sankey.vue';

</script>

<style scoped> 
.mainPage{
   display: flex;
   flex-direction: column;
   background-color: rgba(50, 50, 50, 0.3);
   backdrop-filter: blur(5px);
   margin: 10px;
   width: calc(100% - 30px);
   height: calc(100% - 30px);
   border: 5px solid rgba(50, 50, 50, 1);
   border-radius: 5px;
}

.row {
   display: flex;
}

.firstRow {
   flex: 1.75;
}

.secondRow {
   flex: 1;
}

.container {
   flex: 1;
   border: 1px solid black;
   padding: 10px;
   justify-content: center;
   align-items: center;
}

.firstRow .container:first-child,
.firstRow .container:last-child {
   flex: 1;
}

.firstRow .container:nth-child(2) {
   flex: 3;
}

.secondRow .container:nth-child(2) {
   flex: 3;
}

.macos {
   background-color: rgba(255, 255, 255,0.9);
   backdrop-filter: blur(5px);
   flex: 1;
   padding: 10px;
   border: 3px solid black;
   border-radius: 10px;
   width: full;
 }
</style>