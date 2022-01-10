<template>
  <view class="navTabBox">
    <view class="longTab">
      <scroll-view
        scroll-x="true"
        style="white-space: nowrap; display: flex"
        scroll-with-animation
        :scroll-left="tabLeft"
      >
        <view
          class="longItem"
          :style="&quot;width:&quot;+isWidth+&quot;px&quot;"
          :data-index="index"
          :class="index===tabClick?'click':''"
          v-for="(item,index) in tabTitle"
          :key="index"
          :id="'id'+index"
          @click="longClick(index)"
        >{{ item }}</view>
        <view
          class="underlineBox"
          :style="&quot;transform:translateX(&quot;+isLeft+&quot;px);width:&quot;+isWidth+&quot;px&quot;"
        >
          <view class="underline"/>
        </view>
      </scroll-view>
    </view>
  </view>
</template>

<script>
export default {
  name: 'NavTab',
  props: {
    tabTitle: {
      type: Array,
      default: [],
    },
    tabChosen: {
      type: Number,
      default: 0,
    },
  },
  data() {
    return {
      tabClick: 0, // 导航栏被点击
      isLeft: 0, // 导航栏下划线位置
      isWidth: 0, // 每个导航栏占位
      tabLeft: 0,
    };
  },
  created() {
    console.log('tabChosen' + this.tabChosen);

    var that = this;
    // 获取设备宽度
    uni.getSystemInfo({
      success(e) {
        if (that.tabTitle.length <= 5) {
          that.isWidth = e.windowWidth / that.tabTitle.length; // 宽度除以导航标题个数=一个导航所占宽度
        } else {
          that.isWidth = e.windowWidth / 5;
        }
        that.isLeft = that.tabChosen * that.isWidth;
        that.tabClick = that.tabChosen;
      },
    });
  },
  methods: {
    // 导航栏点击
    longClick(index) {
      if (this.tabTitle.length > 5) {
        var tempIndex = index - 2;
        tempIndex = tempIndex <= 0 ? 0 : tempIndex;
        this.tabLeft = (index - 2) * this.isWidth; // 设置下划线位置
      }
      console.log('index' + index);
      if (index === 0) {
        uni.redirectTo({
          url: '/pages/search/search?newindex=0',
          animationType: 'pop-in',
          animationDuration: 200,
          success: function() {
            console.log('success');
          },
          fail: function(res) {
            console.log('fail', res);
          },
        });
      } else if (index === 1) {
        uni.redirectTo({
          url: '/pages/recommondation/shake?newindex=1',
          animationType: 'pop-in',
          animationDuration: 200,
        });
      } else if (index === 2) {
        uni.redirectTo({
          url: '/pages/user/user?newindex=2',
          animationType: 'pop-in',
          animationDuration: 200,
        });
      }
      this.$emit('changeTab', index);// 设置swiper的第几页
      // this.$parent.currentTab = index //设置swiper的第几页
    },
  },
};
</script>

<style lang="scss">
	.navTabBox {
		width: 100vw;
		color: rgba(70, 70, 70, 0.5);
		.click {
			color: #442918;
		}
		.longTab {
			width: 100%;
			.longItem{
				height: 90upx;
				display: inline-block;
				line-height: 90upx;
				text-align: center;
        font-weight: bolder;
			}
			.underlineBox {
				height: 3px;
				width: 20%;
				display: flex;
				align-content: center;
				justify-content: center;
				transition: .5s;
				.underline {
					width: 84upx;
					height: 4px;
					background-color: #442918;
				}
			}
		}
	}
</style>
