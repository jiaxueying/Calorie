<template>
  <view>
    <view class="container">
      <img
        id="img1"
        src="https://nkucalorie.top:8000/media/static/background.jpg"
      >
      <img
        id="img2"
        src="https://nkucalorie.top:8000/media/static/background.jpg"
      >
      <view class="header">
        <image
          :src="'../../static/icon.png'"
          style="width:100px; height:100px;display: block;"
        /></image>
      </view>

      <view class="main">
        <view
          class="mybutton"
          hover-class="hover-button"
        >
          <navigator url="../search/search">菜品查询</navigator>
        </view>
        <view
          class="mybutton"
          hover-class="hover-button"
        >
          <navigator url="../recommondation/shake">菜品推荐</navigator>
        </view>
        <view
          class="mybutton"
          hover-class="hover-button"
        >
          <navigator url="../user/user">用户中心</navigator>
        </view>
        <view
          class="mybutton"
          hover-class="hover-button"
        >
          <navigator url="about">关于“粟”</navigator>
        </view>

      </view>

    </view>
  </view>
</template>

<script>
import {
  backendUrl,
  request,
} from '@/common/helper.js';

export default {
  data() {
    const currentDate = this.getDate({
      format: true,
    });
    return {
      date: currentDate,

    };
  },
  computed: {
    startDate() {
      return this.getDate('start');
    },
    endDate() {
      return this.getDate('end');
    },
  },
  methods: {

    bindDateChange: function(e) {
      var txt = '';
      txt += e.target.value[8];
      txt += e.target.value[9];
      this.date = txt;
      uni.showToast({
        title: '日期切换成功',
        duration: 2000,
      });
    },

    getDate(type) {
      const date = new Date();
      let year = date.getFullYear();
      let month = date.getMonth() + 1;
      let day = date.getDate();

      if (type === 'start') {
        year = year - 60;
      } else if (type === 'end') {
        year = year + 2;
      }
      month = month > 9 ? month : '0' + month;
      day = day > 9 ? day : '0' + day;
      return `${day}`;
    },
  },

  onLoad() {
    uni.setStorageSync('meal-list', []);

    uni.login({
      success: (res) => {
        console.log(res.code);
        uni.request({
          url: 'https://nkucalorie.top:8000/user/login/',
          data: {
            code: res.code,
            name: '123',
          },
          method: 'POST',
          success: (res) => {
            console.log('log successfully');
            console.log(res);
            uni.setStorage({
              key: 'token',
              data: res.data.token,
            });
          },
        });
      },
    });

    uni.getStorage({
      key: 'weightdate',
      success: (res) => {
        console.log(res);
      },
      fail: () => {
        uni.setStorage({
          key: 'weightdate',
          data: 60,
          success: () => {
            console.log('set weightdate');
          },
        });
      },
    });

    uni.getStorage({
      key: 'meal-list',
      success: (res) => {
        console.log(res);
      },
      fail: () => {
        uni.setStorage({
          key: 'meal-list',
          data: [],
          success: () => {
            console.log('set meal-list');
          },
        });
      },
    });
  },

};

/* export default {
      components:{
        recrange,
        DateChooser
      },
  		data() {
  			return {
          isfirst:false,
  				msg:'点击此处选择餐品时间段',
          isrange:false,
          date:"",
          isdate:false,
  			}
  		}, */
</script>

<style>
  #img1 {
    position: fixed;
    top: 0;
    height: 85%;
    width: 100%;
    z-index: -1;

  }

  #img2 {
    position: fixed;
    top: 15%;
    height: 85%;
    width: 100%;
    z-index: -1;
  }

  .header {
    /* position: absolute; */
    top: 10%;
  }

  .header>p {
    font-size: 60rpx;
    font-family: Arial, Helvetica, sans-serif;
    font-weight: 800;
    color: rgba(80, 80, 80, 0.6);

  }

  .container {
    width: 100%;
    height: 100%;
    /* background-color: rgba(115, 97, 89, 1); */
    background-color: rgb(219, 207, 202);
    position: fixed;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-evenly;
    overflow: hidden;
  }

  .main {
    width: 90%;
    height: 40%;
    display: flex;
    flex-wrap: wrap;
  }

  .main>.button {
    box-sizing: border-box;
    margin: 5%;
    width: 40%;
    height: 40%;
    border: rgba(219, 207, 202, 0.8) 10rpx solid;
    border-radius: 15%;
    display: flex;
    justify-content: center;
    align-items: center;
    color: rgba(89, 69, 61, 0.8);
    font-size: 50rpx;
    font-weight: bold;
  }

  .main>.date {
    border-radius: 5%;
    width: 34%;
    margin-left: 8%;
    display: flex;
    flex-direction: column;
    border: rgba(219, 207, 202, 100) 15rpx solid;
  }

  .bar {
    width: 100%;
    line-height: 50%;
    visibility: hidden;
  }

  picker {
    width: 100%;
    text-align: center;
  }

  .uni-input {
    width: 100%;
    border-top: rgba(219, 207, 202, 100) 15rpx solid;
    font-size: 85rpx;
  }

  .hover-button {
    background-color: rgba(219, 207, 202, 0.2);
  }

  .mybutton {
    width: 50%;
    height: 20%;
    display: flex;
    position: relative;
    margin: 10px;
    padding: 0 20px;
    text-align: center;
    text-decoration: none;
    font: 12px/25px Arial, sans-serif;
    font-size: 40rpx;
    background-color: rgba(217, 207, 202, 1);
    color: rgb(65, 38, 59, 0.7);
    border-radius: 10px;
    margin: auto;
    align-items: center;
    justify-content: center;
  }
</style>
