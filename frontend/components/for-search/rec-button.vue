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
		margin: 11rpx 15rpx 11rpx 0rpx;
		font-size: 20rpx;
		display:inline-block;
		border-radius: 26rpx;
		border: 3rpx solid #000000;
		background-color: #FFFFFF;
    padding-left: 30rpx;
    padding-right: 30rpx;
	}
</style>
