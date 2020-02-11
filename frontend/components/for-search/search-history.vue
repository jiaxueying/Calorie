<template>
	<view class="SearchHistory">
		<view class="SearchHistoryName">●&nbsp;{{viewname}}</view>
		<view class="historyDetail" v-for="n in names" :key="n">
			<rec-button :name="n"></rec-button>
		</view>
	</view>
</template>

<script>
	import RecButton from "./rec-button.vue"
	export default {
		components: {
			RecButton,
		},
		props: {
			viewname: {
				type: String,
				default: "",
			},
		},
		data() {
			return {
				names: ["1","22222","3","44444444","1","22222","3","44444444","1","22222","3","44444444"],
			}
		},
	}
</script>

<style>
	.SearchHistory {
		float:left;
		width: 100%;
    padding-left: 20rpx;
    padding-right: 20rpx;
    margin-top: 25rpx;
    box-sizing:border-box;

	}
  .SearchHistoryName {
    padding: 15rpx 0;
  }
  .historyDetail {
    padding-left:20rpx;
  }
</style>
