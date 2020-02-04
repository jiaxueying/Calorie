<template>
  <view class="content">
  <view class="content1">
    <input type="checkbox" name="check" value=" ">
    <image style="width: 100px;height: 100px" src="../../static/logo.png"></image>
  </view>
  <view class="content2">
    <view class="content2a">
      <h2>{{meal-name}}</h2>
    </view>
    <view class="content2b">
      <p>{{calorie}}</p>
      <picker range="number"></picker>
    </view>
  </view>
  </view>
</template>

<script>
  export default {
    props: [],
    methods: {      
   
     },
     data() {
       return {
         'meal-name':'菜品名称',
         calorie:'200',
         number:['one','two','three','four']
       };
     },
     
     }
  
  
</script>

<style>
  .content{
    display:flex;
    flex-direction: row;
  }
  .content1{
    position: relative;
    left:10%;
    top:0px;
    display: inline-block;
  }
  .content2{
    position: relative;
    top:18px
  }
</style>
