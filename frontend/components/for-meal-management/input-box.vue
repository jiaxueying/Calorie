<!-- TODO:change and button css-->

<template>
	<view class="out">
		<input v-model=value id="in" placeholder="你可以在这里搜索" class="inbox" @change="search($event)"/>
		<button class="tableware-icon" @tap="openAddMealList" v-if="show_button">添加菜品</button>
	</view>
</template>

<script>
	export default {
		props: ["show_button"],
		data() {
			return {
				value: '',
			}
		},
    onLoad() {
    },
		methods: {
      openAddMealList:function() {
        console.log("添加菜品 button clicked");
        wx.navigateTo({
          url:"../../pages/dishinfo/add",
        });
      },
      search:function(event) {
          console.log("search in /components/for-meal-management/input-box.vue:" + event.target.value);
          if(event.target.value == "") {
            console.log("try to search empty string, do nothing!");
            return;
          }
          uni.$emit("meal-management-search", event.target.value);
          console.log("meal-management-search emit completed!");
      },
		}
	}
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
		padding-left: 15rpx;
		padding-right: 220rpx;
		font-size: 50rpx;
		border: 1rpx solid #cecece;
		border-radius: 30rpx;
	}
	.tableware-icon {
		height: 70rpx;
		width: 200rpx;
		position: absolute;
    right: 0;
    top: 0;
		margin: 7rpx 10rpx 0 5rpx;
		border: 1rpx #FFFFFF;
		border-radius: 30rpx;
    font-size: 30rpx;
	}
</style>
