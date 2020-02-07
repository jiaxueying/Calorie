<template>
  <view class="content">
    <view class="popup">
      <view style="display: flex;flex-direction: column;justify-content: flex-end;">
      <view style="display: flex;justify-content: center;"><image src="../../static/success.png" class="img"></image></view>
      <view style="display: flex;justify-content: center;"><text class="text">添加成功!</text></view>
      <view class="buttomarea">
        <view class="button" @click="gotoshake">继续摇一摇</view>
        <view class="button" @click="gotohome">返回首页</view>
      </view>
      </view>
    </view>
  </view>
</template>

<script>
  export default{
    methods:{
      gotoshake:function(){
        uni.redirectTo({
          url:"../../pages/recommondation/shake"
        })
      },
      gotohome:function(){
        uni.reLaunch({
          url:"../../pages/index/index"
        })
      }
    }
  }
</script>

<style>
.content{
  display: flex;
  justify-content: center;
  position: fixed;
  width: 100%;
  height:100%;
  background-color: rgba(0,0,0,.30);
}
.popup{
  display: flex;
  justify-content: center;
  width: 70%;
  height: 25%;
  margin-top: 45%;
  background-color: #ffffff;
  border: 1px #333333 solid;
  border-radius: 10px;
}
.img{
  height: 160rpx;
  width: 160rpx;
}
.text{
  margin-bottom: 8%;
}
.buttomarea{
  display: flex;
  width: 525rpx;
  height: 100rpx;
}
.button{
  width: 50%;
  height: 100%;
  background-color: #ffffff;
  color: #007AFF;
  text-align: center;
  border-radius: 10px;
  line-height: 100rpx;
}
</style>
