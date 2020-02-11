<template>
  <view class="content">
    <text>本餐推荐的卡路里范围为{{min}}-{{max}}cal</text>
  </view>
</template>

<script>
  export default {
   	data() {
  		return {
        min:'',
        max:''
  		}
  	},
    methods:{
     
    }
  }
</script>

<style>
.content{
  display: flex;
  border:#000000 1rpx solid;
  justify-content: center;
  font-size: 1.7em;
  font-weight: 400;
  }
  text{
    line-height: 200%;
    color:#505050;
  }
</style>
