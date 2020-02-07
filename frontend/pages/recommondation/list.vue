<template>
  <view>
    <view class="title">
      <div class="text1">今日推荐</div>
    </view> 
    <view>
      <Meal></Meal>
    </view>
  </view>
</template>

<script>
  import Meal from '../../components/recommodation/recommend.vue'
   export default {
     components: {
      Meal,
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
    },
  };
</script>

<style>
  .title{
    background: rgba(219,207,202,.3); 
    height:50px;
    color:#59453d;
    display: flex;
    flex:2; 
    justify-content: center;
    align-items: center;
  }
</style>
