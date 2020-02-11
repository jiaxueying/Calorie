<template>
	<view class="out">
		<button class="tableware-icon" @tap="ShowOrders()"></button>
		<input name="in" class="inbox" @focus="ShowHistory()" @blur="HideHistory()" />
		<button class="search-icon"></button>
	</view>
</template>

<script>
	export default {
		props: {
			placehold: {
				type: String,
				default: "你可以在这里搜索", 
			}
		},
		data() {
			return {
				
			}
		},
		methods: {
			ShowOrders() {
				console.log("tableware button clicked");
				uni.$emit("showorders");
			},
			ShowHistory() {
				console.log("focused");
				uni.$emit("showhistory");
			}, 
			HideHistory() {
				console.log("blurred");
				uni.$emit("hidehistory");
			}
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
		padding-left: 75rpx;
		font-size: 50rpx;
		border: 1rpx solid #000000;
		border-radius: 5rpx;
	}
	.tableware-icon {
		height: 79rpx;
		width: 75rpx;
		position: absolute;
		margin: 1rpx 0 0 1rpx;
		background-image: url(../../static/tableware.jpg);
		background-repeat: no-repeat;
		background-position: 0 5rpx;
		background-size: 75rpx;
		border: none;
	}
</style>
