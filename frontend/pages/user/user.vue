<template>
	<view class="all">
		<view class="userimg">
			<open-data type="userAvatarUrl"></open-data>
		</view>
		<view class="userinfor">
      <open-data type="userNickName" style="font-size: 2em;height:85rpx;"></open-data>
      <text style="font-size: 1.2em;line-height: 200%;">体重：{{weight}}kg\n</text>
      <text style="font-size: 0.7em;">本日推荐摄入卡路里范围：\n{{minCalForDay}}kcal-{{maxCalForDay}}kcal</text>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
        weight:'100',
        minCalForDay:'1000',
        maxCalForDay:'1500'			
			}
		},
		methods: {
			
		}
	}
</script>

<style>
  .all{
    display: flex;
  }
	.userimg{
    margin-top: 15%;
		width:200rpx;
		height:200rpx;
		border-radius:50%;
    overflow: hidden;
    position:relative;
    left:55rpx;
	}
  .userinfor{
    color: #505050;
    margin-top: 15%;
    display: flex;
    flex-direction: column;
    position:relative;
    left:100rpx
  }
</style>
