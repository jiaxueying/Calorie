<template>
  <view class="orders">
    <view class="orderHead">
      <view class="head_one">
        <view class="image_head">
          <open-data
            type="userAvatarUrl"
          />
        </view>
        <view class="name_head">我的菜单</view>
        <view class="cont_head">{{ Calories }}kcal</view>
      </view>
      <!-- <view class="cancel_head"><view class="button" @click="clrAll">清空</view></view> -->
    </view>
    <view class="orderMid">
      <!--推荐卡路里摄入范围-->
      <recommendrange
        :min="min"
        :max="max"
      />
    </view>
    <view
      class="order_list"
      v-for="food in Foods"
      :key="food.name"
    >
      <food-in-order
        :foodname="food.name"
        :weight="food.sum"
        :calorie="food.cal"
      />
    </view>
    <view class="order_bottom">
      <button @tap="clrAll">
        <text
          class="iconfont icon-delete"
          style="color:#442918"
        />
        {{ text1 }}</button>
      <button @tap="Close()">
        <text
          class="iconfont icon-addToList"
          style="color:#442918"
        />
        {{ text2 }}</button>
      <button @tap="mylist">
        <text
          class="iconfont icon-caidan"
          style="color:#442918"
        />
        {{ text3 }}</button>
    </view>
  </view>
</template>

<script>

import FoodInOrder from './food-in-order.vue';
export default {
  components: {
    FoodInOrder,
  },
  props: {
    Foods: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      Calories: 0,
      min: 40,
      max: 50,
      text1: '  全部清空',
      text2: '  继续添加',
      text3: '   生成菜单',
    };
  },
  created() {
    // console.log('你好');
    uni.request({
      url: 'https://calorie.liyangpu.com:8003/user/profile/',
      method: 'GET',
      header: {
        Authorization: 'Token ' + uni.getStorageSync('token'),
      },
      success: (res) => {
        console.log('nihao');
        this.min = res.data.data.min_calorie;
        this.max = res.data.data.max_calorie;
      },

    });
    uni.$on('CalChange', this.caloriesChange);
    uni.$on('delname', this.delName);
  },
  methods: {
    Close() {
      console.log('add button clicked');
      this.$parent.IsShow = false;
    },
    caloriesChange(v) {
      console.log(v);
      this.Calories += v;
    },
    delName(v) {
      console.log('DelName activated');
      var i = 0;
      for (; i < this.Foods.length; i++) { if (this.Foods[i].name == v) break; }
      this.Foods.splice(i, 1);
      for (i = 0; i < this.Foods.length; i++) { console.log(this.Foods[i]); }
    },
    clrAll() {
      uni.setStorageSync('meal-list', []);
      uni.$emit('refresh1');
      uni.$emit('refresh2');
    },
    mylist() {
      this.Close();
      console.log('mylist clicked');
      uni.removeStorageSync('historymsg');
      if (this.Foods.length === 0) {
        uni.showModal({
          title: '提示',
          content: '您的购物车中还没有菜品哦~',
        });
        return;
      }
      this.$parent.IsShow = false;
      wx.navigateTo({
        url: '../others/mylist',
      });
    },
  },
  watch: {
    Foods(newV) {
      console.log('Foods changed');

      this.Calories = 0;
      for (var i = 0; i < newV.length; i++) {
        console.log('Here');
        console.log(newV[i]);
        this.Calories += newV[i].cal * newV[i].sum;
      }
    },
  },
};

</script>

<style lang="less">
  text{
    white-space: pre;
  }
  .orderMid{
    background-color: #f4f1ec;
  }
  recommendrange {
   position:relative;
   right:80rpx;
   }

//@import '/src/assets/iconfont/iconfont.css';

  .icon-tianjia{
    font-size: 25px;
            position: fixed;
            top: 20px;
            right: 10px;

  }
  .orders {
    width: 100%;
    display: inline-block;
    .orderHead {
      background-color: #f4f1ec;
      border-radius: 0 30px 0 0;
      box-shadow: 2px -0.5px 4px 0px rgba(0, 0, 0, 0.1);a
      height: 110rpx;

      .head_one {
        height: 50rpx;

        .image_head {
          width: 86rpx;
          height: 86rpx;
          position: relative;
          top: -20rpx;
          left: 10rpx;
          background-color: #ccc;
          float: left;
          border-radius: 15rpx;
        }

        .name_head {
          // position: relative;
          float: left;
          margin-left: 20rpx;
          line-height: 86rpx;
          color: #442018;
          font-size: 28rpx;
          font-weight: 300;
        }

        .cont_head {
          float: right;
          width: 113rpx;
          height: 50rpx;
          font-size: 26rpx;
          line-height: 86rpx;
          text-align: center;
        }
      }

      .cancel_head {
        text-align: right;

        .button {
          background-color: rgba(0, 0, 0, 0);
          font-size: 24rpx;
          color: rgba(80, 80, 80, 1);
          display: inline-block;
          margin-right: 20rpx;
        }
      }
    }

    .order_list {
      padding: 10rpx 20rpx;
      background-color: rgb(239, 239, 241);
    }
    .order_bottom{
      display: flex;
      justify-content: space-between;
      align-items: center;
      background-color: #fff;

      image{
          width: 30rpx;
          height: 30rpx;

        }

        button {
          font-size: 28rpx;
          font-weight: bolder;
          background-color: #ffffff;
          color: #602808;
          box-sizing: border-box;
          width: 33%;
        }

    }
  }
</style>
