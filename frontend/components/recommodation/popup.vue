//添加成功弹出框
<template>
  <view class="content">
    <view class="popup">
      <view class="popup_1">
        <view class="popup_2">
          <image
            class="img"
            src="../../static/success.png"
          /></image></image>
          <text>添加成功!</text>
        </view>
        <view class="buttomarea">
          <view
            class="button"
            @click="gotoshake"
          >重新推荐</view>
          <view
            class="button"
            @click="gotohome"
          >返回首页</view>
        </view>
      </view>
    </view>
  </view>
</template>

<script>
export default {
  methods: {
    gotoshake: function() {
      uni.redirectTo({
        url: '../../pages/recommondation/shake',
      });
    },
    gotohome: function() {
      uni.navigateBack({
        delta: 99,
      });
    },
  },
};
</script>

<style>
 image{
   width:160rpx;
   height: 140rpx;
    }
.content{
  display: flex;
  justify-content: center;
  position: fixed;
  width: 100%;
  height:100%;
  background-color: rgba(0,0,0,0.3);
}
.popup{
  display: flex;
  justify-content: center;//popup1会居中
  width: 70%;
  height: 25%;
  margin-top: 45%;
  background-color: #ffffff;
  border-radius: 10px;
}
.popup_1{
display: flex;
flex-direction: column;//改变主轴方向,纵向为主轴
justify-content: flex-end;//popup2,text,button向下对齐
}
.popup_2{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.img{
  height: 150rpx;
  width: 150rpx;
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
  color: #59453d;
  text-align: center;
  line-height: 100rpx;
  border-radius: 20rpx;
}
</style>
