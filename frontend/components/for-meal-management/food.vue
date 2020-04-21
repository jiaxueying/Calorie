<!-- TODO:add url in openDetail
     TODO:change src in image-->

<template>
  <view class="food">
    <checkbox v-if="show_radio_button" class="radioButton" @tap="changeCheckedStatus($event)">
    </checkbox>
    <image 
      class="listImg"
      :src="'../../static/' + food.pic"
      mode=""
      @tap="openDetail"
    />
    <view class="listText" @tap="openDetail">
      <text>{{food.name}}</text>
    </view>
  </view>
</template>

<script>
  export default {
    props: ['food', 'show_radio_button'],
    data() {
      return {
        checked: false,
      }
    },
    methods: {
      changeCheckedStatus:function(event) {
        this.checked = !this.checked;
        if(this.checked){
          console.log(this.food.name + " checked");
          uni.$emit("add-checked-meal-list", this.food);
        }
        else {
          console.log(this.food.name + " unchecked");
          uni.$emit("remove-checked-meal-list", this.food);
        }
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
  .radioButton {
    margin: auto;
    padding-right: 20rpx;
  }
</style>
