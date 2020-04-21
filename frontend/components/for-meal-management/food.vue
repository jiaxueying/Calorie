<!-- TODO:add url in openDetail
     TODO:change src in image-->

<template>
  <view>
    <view class="food" @tap="openDetail">
      <image 
        class="listImg"
        :src="'../../static/' + food.pic"
        mode=""
      />
      <view class="listText">
        <text>{{food.name}}</text>
      </view>
    </view>
  </view>
</template>

<script>
  export default {
    props: ['food'],
    data() {
      return {
      }
    },
    methods: {
      changeCheckedStatus:function(event) {
        event.target.set
        if(event.target.checked)console.log(this.food.name + " checked");
        else console.log(this.food.name + " unchecked");
      },
      openDetail:function() {
        console.log(this.food.name + " clicked");
        wx.navigateTo({
          url:""
        });
      }
    },
  }
</script>

<style>
  .listImg {
    flex:1;
    width: 160rpx;
    height: 160rpx;
  }
  .listText {
    margin: auto;
    flex:2;
    float:right;
    padding-left: 175rpx;
  }
  .food {
    display: flex;
    margin: 15rpx 30rpx 15rpx 30rpx;
  }
</style>
