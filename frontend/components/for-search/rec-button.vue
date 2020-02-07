<template>
	<button class="BtnInSearch">{{name}}</button>
</template>

<script>
	export default {
		props: {
			name: {
				type: String,
				default: "",
			}
		}
	}
</script>

<style>
	.BtnInSearch {
		float:left;
		margin: 5rpx 5rpx 5rpx 5rpx;
		font-size: 20rpx;
		display:inline-block;
		border-radius: 16rpx;
		border: 3rpx solid #000000;
		background-color: #FFFFFF;
	}
</style>
