<template>
  <view class="content">
    <view class="nav">
      <navTab
        ref="navTab"
        :tab-title="tabTitle"
        :tab-chosen="1"
        @changeTab="changeTab"
      />
    </view>

    <view class="all">
      <image
        src="https://calorie.liyangpu.com:8003/media/static/shake.png"
        class="img"
      /></image>
      <text class="text">摇一摇来发现美食吧！</text>

    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      currentTab: 1, // sweiper所在页
      tabTitle: ['菜品查询', '菜品推荐', '个人中心'], // 导航栏格式
    };
  },
  onLoad() {
    uni.onAccelerometerChange(function(a) {
      let b = a.x * a.y * a.z;
      console.log(b);
      if (b > 0.5 || b < -0.5) {
        console.log('success');
        uni.stopAccelerometer();
        uni.redirectTo({
          url: './list',
        });
      }
    });
  },
  onUnload() {
    uni.stopAccelerometer();
  },
  methods: {
    changeTab(index) {
      this.currentTab = index;
    },
    swiperTab: function(e) {
      var index = e.detail.current; // 获取索引
      this.$refs.navTab.longClick(index);
    },

    gotolist() {
      uni.redirectTo({
        url: 'list',
      });
    },

  },
};
</script>

<style>
  .nav {
    left: 0;
    top: 0;
    color: #C8A57E;
    width: 100vw;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    font-size: 24upx;
    background-color: #FFFFFF;
    z-index: 99999;
    }

  .content {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .img {
    width: 300px;
    height: 300px;
    margin: 0 auto;
  }

  .text {
    text-align: center;
    font-size: 28rpx;
  }
  .all{
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
</style>
