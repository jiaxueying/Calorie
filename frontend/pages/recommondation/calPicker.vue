<template>
  <view v-show="isshow" class="picker">
    <picker mode="multiSelector" range='cal' value=0></picker>a
  </view>
</template>

<script>
export default{
  props:['isshow'],
  data() {
    return{
      cal:[
        ['a','b'],
        ['c','d']
      ]
    }
  },
}
</script>

<style>
.picker{
  height: 200rpx;
  width: 200rpx;
  margin-top: 200rpx;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 50rpx;
}
</style>
