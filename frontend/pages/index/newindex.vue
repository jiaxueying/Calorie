<template>
  <view>
  <view class="container">
      <img id="img1" src="../../static/background.jpg"/>
      <img id="img2" src="../../static/background.jpg"/>
      <view class="header">
          <p>首页</p>
      </view>
      
      <view class="main">
          <view class="button" hover-class="hover-button">
              <navigator url="../search/search">点餐处</navigator>
          </view>
          <view class="button date" hover-class="hover-button">
                <view class="bar">.....</view>
                <picker mode="date" :value="date" :start="startDate" :end="endDate" @change="bindDateChange">
                    <view class="uni-input">{{date}}</view> 
                </picker>
          </view>
          <view class="button" hover-class="hover-button">
              <navigator url="../recommondation/range">营养推荐</navigator>
          </view>
          <view class="button" hover-class="hover-button">
              <navigator url="../user/user">用户中心</navigator>
          </view>
      </view>
      
  </view>
  </view>
</template>

<script>
  export default {
      data() {
          const currentDate = this.getDate({
              format: true
          })
          return {
              date: currentDate,
          }
      },
      computed: {
          startDate() {
              return this.getDate('start');
          },
          endDate() {
              return this.getDate('end');
          }
      },
      methods: {
          bindDateChange: function(e) {
            var txt="";
            txt+=e.target.value[8];
            txt+=e.target.value[9];
            this.date = txt
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
              month = month > 9 ? month : '0' + month;;
              day = day > 9 ? day : '0' + day;
              return `${day}`;
          }
      }
  }
</script>

<style>
  #img1{
    position: fixed;
    top:0;
    height: 85%;
    width:100%;
    z-index:-1;
    
  }
  #img2{
    position: fixed;
    top:15%;
    height: 85%;
    width:100%;
    z-index:-1;
  }
  .header{
    position: absolute;
    top:5%;
  }
  .header>p{
    font-size: 60rpx;
    font-family: Arial, Helvetica, sans-serif;
    font-weight: 800;
    color: rgba(80,80,80,0.6);
    
  }
  .container{
    width:100%;
    height:100%;
    position: fixed;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-evenly;
    overflow: hidden;
  }
  .main{
    width:90%;
    height:40%;
    display: flex;
    flex-wrap: wrap;
  }
  .main>.button{
    box-sizing: border-box;
    margin: 5%;
    width: 40%;
    height:40%;
    border: rgba(219,207,202,0.8) 10rpx solid;
    border-radius: 15%;
    display: flex;
    justify-content: center;
    align-items: center;
    color: rgba(89,69,61,0.8);
    font-size: 50rpx;
    font-weight: bold;
  }
  .main>.date{
    border-radius:5% ;
    width: 34%;
    margin-left: 8%;
    display: flex;
    flex-direction: column;
    border: rgba(219,207,202,100) 15rpx solid;
    
  }
  .bar{
    width: 100%;
    line-height: 50%;
    visibility: hidden;
  }
  picker{
    width: 100%;
    text-align: center;
  }
  .uni-input{
    width: 100%;
    border-top: rgba(219,207,202,100) 15rpx solid;
    font-size: 85rpx;
  }
  .hover-button{
    background-color: rgba(219,207,202,0.2);
  }
</style>
