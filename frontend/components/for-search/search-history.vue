<template>
	<view class="SearchHistory">
		<view>{{viewname}}</view>
		<view v-for="n in names" :key="n">
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
	}
</style>
