<template>
  <Meal></Meal>
  <input type="button" @click="toPath" value="nextpage">
</template>

<script>
  import Meal from './recommend.vue'
   export default {
     components: {
      Meal
    },
    data() {
      return {
      };
    },
   
    onLoad() {
        
    },
    onPullDownRefresh(){
      
    },
    methods: {
      toPath(){
        uni.switchTab({
          url:"./recommend"
        })
      }
  
    },
  };
</script>

<style>
</style>
