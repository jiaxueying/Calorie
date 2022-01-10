<template>
  <button
    class="BtnInSearch"
    @tap="search"
  >{{ name }}</button>
</template>

<script>
export default {
  props: {
    name: {
      type: String,
      default: '',
    },
  },
  methods: {
    search() {
      uni.$emit('search_key', this.name);
    },
  },
};
</script>

<style>
.BtnInSearch {
float:left;
margin: 11rpx 15rpx 11rpx 0rpx;
font-size: 20rpx;
display:inline-block;
border-radius: 26rpx;
border: 4rpx solid #8F8F94;
background-color: #FFFFFF;
    padding-left: 30rpx;
    padding-right: 30rpx;
    color:#555C60;
}
</style>
