import SizeInfo from '@/components/info/sizeInfo.vue';
import { defineStore } from 'pinia';

export const useStatesStore = defineStore({
  id: 'myStore',
  state: () => ({
    d3States: {
      zoom: false,
    } as Record<string, boolean>,   

    componentVisibility: {
      mainInfo: true,
      sizeInfo: false,
      chartsInfo: false,
      selectInfo: false,
    } as Record<string, boolean>, 
    
  }),
  actions: {
    showComponent(componentName: string) {
      this.componentVisibility[componentName] = true;
    },
    hideComponent(componentName: string) {
      this.componentVisibility[componentName] = false;
    },
    toggleComponent(componentName: string) {
      this.componentVisibility[componentName] = !this.componentVisibility[componentName];
    },
  }
})
