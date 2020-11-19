<template>
  <view class="content">
    <image src="https://nkucalorie.top:8000/media/static/shake.png" class="img"></image>
    <text class="text">摇一摇来发现美食吧！</text>
    <button @click="gotolist" style="margin-top: 50rpx;">调试专用作弊按钮</button>
  </view>
</template>

<script>
  export default {
    data() {
      return {

      }
    },
    onLoad() {
      uni.onAccelerometerChange(function(a) {
        let b = a.x * a.y * a.z
        console.log(b)
        if (b > 0.5 || b < -0.5) {
          console.log("success")
          uni.stopAccelerometer()
          uni.redirectTo({
            url: "./list"
          })
        }
      })
    },
    onUnload() {
      uni.stopAccelerometer()
    },
    methods: {
      gotolist() {
        uni.redirectTo({
          url: "list"
        })
      }

    }
  }
</script>

<style>
  .content {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 40%;
  }

  .img {
    width: 300px;
    height: 300px;
    margin: 0 auto;
  }

  .text {
    width: 750rpx;
    text-align: center;
    font-size: 50rpx;
  }
</style>
