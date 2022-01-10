<template>
  <view class="content">
    <text>本日推荐的卡路里范围为{{ min }}-{{ max }}cal</text>
  </view>
</template>

<script>
export default {
  props: ['min', 'max'],
  // 子组件
    	data() {
   		return {

   		};
   	},
  methods: {

  },
};
</script>

<style>
  .content{
    display: flex;
    //border:#000000 1rpx solid;
    justify-content: center;
    font-size: 29rpx;
    font-weight: 400;
    }
    text{
      line-height: 200%;
      color:#484848;
    }
</style>
