<!-- TODO:add url in openDetail
     TODO:change src in image-->

<template>
  <view class="food">
    <checkbox
      v-if="show_radio_button"
      class="radioButton"
      :checked="ischecked"
      @tap="changeCheckedStatus()"
    />
    <image
      class="listImg"
      :src="'http://cal.hanlh.com:8000'+food.img"
      mode=""
      @tap="openDetail"
    />
    <view
      class="listText"
      @tap="openDetail"
    >
      <text>{{ food.dish }}\n</text>
      <text v-if="show_count">份数：{{ food.num }}</text>
    </view>
  </view>
</template>

<script>
export default {
  props: ['food', 'show_radio_button', 'ischecked', 'show_count'],
  data() {
    return {
      checked: this.ischecked,
    };
  },
  methods: {
    changeCheckedStatus: function() {
      console.log(this.food.name + ' checkbox clicked');
      uni.$emit('change-checked-meal-list', this.food);
    },
    openDetail: function() {
      console.log(this.food.name + ' clicked');
      wx.navigateTo({
        url: '../../pages/dishinfo/modify?foodDetail=' + JSON.stringify(this.food),
      });
    },
  },
};
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
