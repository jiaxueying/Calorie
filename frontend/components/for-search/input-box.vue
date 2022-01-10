<template>
  <view class="out">
    <button
      class="tableware-icon"
      @tap="ShowOrders()"
    />
    <!-- <input v-model=value id="in" class="inbox" @change="search($event)" @focus="ShowHistory()" @blur="HideHistory($event)" /> -->
    <input
      v-model="value"
      id="in"
      class="inbox"
      @change="search($event)"
    >
    <button class="search-icon"/>
  </view>
</template>

<script>
export default {
  props: {
    placehold: {
      type: String,
      default: '你可以在这里搜索',
    },
  },
  data() {
    return {
      value: '',
    };
  },
  onLoad() {
    uni.$on('setInputValue', this.setValue);
  },
  methods: {
    ShowOrders() {
      console.log('tableware button clicked');
      uni.$emit('showorders');
    },
    ShowHistory() {
      console.log('focused');
      uni.$emit('showhistory');
    },
    HideHistory(event) {
      console.log('blurred');
      uni.$emit('hidehistory');
      uni.$emit('addHistory', event.target.value);
    },
    search(event) {
      console.log('input');
      // uni.$emit("hidehistory");
      uni.$emit('search_key', event.target.value);
    },
    setValue(v) {
      console.log('set value:' + v);
      this.value = v;
    },
  },
};
</script>

<style>
.out {
z-index: 1;
position: fixed;
width: 100%;
background-color: #FFFFFF;
}
.inbox {
height: 80rpx;
padding-left: 120rpx;
font-size: 40rpx;
border: 1rpx solid #d9cfca;
border-radius: 5rpx;
}
.tableware-icon {
height: 79rpx;
width: 75rpx;
position: absolute;
margin: 1rpx 0 0 1rpx;
background-size: 75rpx;
background-image: url(https://calorie.liyangpu.com:8003/media/static/default.jpg);
background-repeat: no-repeat;
border: none;
}
  button::after{
    border: none;
  }
</style>
