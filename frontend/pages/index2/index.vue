<template>
  <view>
   <Meal></Meal>
  </view>
</template>

<script>
  import Meal from './recommend.vue'
   export default {
     components: {
      Meal
    },
    data() {
      return {
        str:'<button>nextpage</button>'
      };
    },
   
    onLoad() {
        
    },
    onPullDownRefresh(){
      
    },
    methods: {
    },
  };
</script>

<style>
</style>
